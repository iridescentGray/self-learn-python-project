import os
import traceback
import paramiko

HOST_NAME="10.150.30.32"
PORT=22
USER_NAME=""
PASSWORD=""

LOCAL_FILE_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)),"test.jar")
REMOTE_FILE_PATH="/home/zhoujianyu231113"

def execute_ssh_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode('utf-8')
    errors = stderr.read().decode('utf-8')
    return output, errors

def check_file_existence(ssh_client,remote_file_path):
    # 执行检查文件是否存在的命令
    check_command = f'sudo stat {remote_file_path}'  # 使用 stat 命令检查文件是否存在
    stdin, stdout, stderr = ssh_client.exec_command(check_command)

    # 检查命令执行结果
    # 如果文件存在，stdout 不会为空 
    # 如果文件不存在，stderr 会有相应的错误信息
    file_exists = not bool(stderr.read().decode().strip())

    return file_exists

try:
    ssl_client = paramiko.SSHClient()
    ssl_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssl_client.connect(hostname=HOST_NAME, port=PORT, username=USER_NAME, password=PASSWORD)
    is_jar_exist=check_file_existence(ssl_client,"/data/workflow/yudao-server.jar")

    # 如果jar包存在，则执行备份
    if(is_jar_exist):
        count_back_file, errors = execute_ssh_command(ssl_client, 'sudo ls /data/workflow/bak | wc -l')
        next_back_file_number=int(count_back_file) + 1
        output, errors  = execute_ssh_command(ssl_client, f'sudo mv /data/workflow/yudao-server.jar /data/workflow/bak/yudao-server.jar.bk{next_back_file_number}')
    sftp_cli=ssl_client.open_sftp()
    print(f"sftp.getcwd():  {sftp_cli.getcwd()}")

    sftp_cli.put(LOCAL_FILE_PATH, REMOTE_FILE_PATH)
    sftp_cli.close()
    ssl_client.close()

except paramiko.AuthenticationException as auth_exception:
    print("Authentication failed:", auth_exception)
except paramiko.SSHException as ssh_exception:
    print("SSH connection failed:", ssh_exception)
except Exception as e:
    print("An error occurred. Exception type:", type(e))
    traceback.print_exc()  # 打印异常堆栈信息