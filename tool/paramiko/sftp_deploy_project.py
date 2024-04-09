import os
import traceback

import paramiko
from tqdm import tqdm

"""
测试环境部署脚本,运行后,自动把target里的yudao-server.jar部署到10.150.30.32

需要配3个变量,
USER_NAME(ssh用户名)
PASSWORD(ssh密码)
REMOTE_USER_HOME_PATH(服务器用户目录,例如/home/zjy ,用于作为文件上传的中转目录）
"""

# 用户配置
HOST_NAME = "10.150.30.32"
# ----------------------------------自定义配置---------------------------------

PORT = 22
USER_NAME = ""
PASSWORD = ""
REMOTE_USER_HOME_PATH = ""  # 文件会先上传到用户目录,作为中转


REMOTE_PROJECT_PATH = "/data/workflow"
DEPLOY_FILE_NAME = "yudao-server.jar"
DEPLOY_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target")
# 需要部署的jar包
LOCAL_FILE_PATH = os.path.join(DEPLOY_FILE_PATH, DEPLOY_FILE_NAME)

# 校验文件是否存在
if not os.path.isfile(LOCAL_FILE_PATH):
    raise ValueError("没有待部署文件")

print(f"----------------------部署文件: {LOCAL_FILE_PATH}")


def execute_ssh_command(ssh_client, command):
    _, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode("utf-8")
    errors = stderr.read().decode("utf-8")
    return output, errors


def check_file_existence(ssh_client, remote_file_path):
    # 执行检查文件是否存在的命令
    check_command = f"sudo stat {remote_file_path}"  # 使用 stat 命令检查文件是否存在
    _, _, stderr = ssh_client.exec_command(check_command)
    # 检查命令执行结果
    # 如果文件存在,stdout 不会为空
    # 如果文件不存在,stderr 会有相应的错误信息
    file_exists = not bool(stderr.read().decode().strip())
    return file_exists


def back_up_file(ssh_client):
    count_back_file, _ = execute_ssh_command(
        ssh_client, f"sudo ls {REMOTE_PROJECT_PATH}/bak | wc -l"
    )
    # 尾缀加一
    next_back_file_number = int(count_back_file) + 1
    execute_ssh_command(
        ssh_client,
        f"sudo mv {REMOTE_PROJECT_PATH}/{DEPLOY_FILE_NAME} {REMOTE_PROJECT_PATH}/bak/{DEPLOY_FILE_NAME}.bk{next_back_file_number}",
    )


def upload_file_to_remote(ssh_client, upload_path):
    sftp_cli = ssh_client.open_sftp()
    try:
        # 开始上传文件
        with sftp_cli.file(upload_path, "wb") as remote_file:
            with open(LOCAL_FILE_PATH, "rb") as local_file:
                with tqdm(
                    total=os.path.getsize(LOCAL_FILE_PATH),
                    unit="B",
                    unit_scale=True,
                    desc="Uploading",
                ) as pbar:
                    while True:
                        buf = local_file.read(32768)  # 读取文件内容
                        if not buf:
                            break
                        remote_file.write(buf)  # 写入到远程文件
                        pbar.update(len(buf))  # 更新进度条
    finally:
        sftp_cli.close()


ssl_client = paramiko.SSHClient()
ssl_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssl_client.connect(hostname=HOST_NAME, port=PORT, username=USER_NAME, password=PASSWORD)

try:
    is_jar_exist = check_file_existence(
        ssl_client, f"{REMOTE_PROJECT_PATH}/{DEPLOY_FILE_NAME}"
    )
    if is_jar_exist:
        # 如果jar包存在,则执行备份,备份到 项目路径/.bak文件夹
        back_up_file(ssl_client)

    remote_file_temp_path = f"{REMOTE_USER_HOME_PATH}/{DEPLOY_FILE_NAME}"
    # 上传到远程用户目录
    upload_file_to_remote(ssl_client, remote_file_temp_path)

    # 复制到真正的项目目录
    remote_file_real_path = f"{REMOTE_PROJECT_PATH}/{DEPLOY_FILE_NAME}"
    execute_ssh_command(
        ssl_client, f"sudo mv {remote_file_temp_path} {remote_file_real_path}"
    )

    # 执行部署脚本 springboot.sh
    deploy_result, _ = execute_ssh_command(
        ssl_client,
        f"cd {REMOTE_PROJECT_PATH} && sudo ./springboot.sh restart {DEPLOY_FILE_NAME} dev",
    )
    print(deploy_result)


except paramiko.AuthenticationException as auth_exception:
    print("Authentication failed:", auth_exception)
except paramiko.SSHException as ssh_exception:
    print("SSH connection failed:", ssh_exception)
except Exception as e:
    print("An error occurred. Exception type:", type(e))
    traceback.print_exc()  # 打印异常堆栈信息
finally:
    ssl_client.close()
