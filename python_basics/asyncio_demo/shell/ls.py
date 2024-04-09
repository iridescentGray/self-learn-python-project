import asyncio
from asyncio.streams import StreamReader
from asyncio.subprocess import PIPE, Process

print(
    "-----------------------------------------ls_print_to_stdout------------------------------------------"
)


async def ls_print_to_stdout():
    process: Process = await asyncio.create_subprocess_exec("ls", "-l")
    print(f"进程的 pid: {process.pid}")
    # 等待子进程执行完毕，并返回状态码
    status_code = await process.wait()
    print(f"status code: {status_code}")


asyncio.run(ls_print_to_stdout())

print(
    "-----------------------------------------ls_print_in_control------------------------------------------"
)


async def ls_print_in_control():
    process: Process = await asyncio.create_subprocess_exec("ls", "-l", stdout=PIPE)
    print(f"进程的 pid: {process.pid}")
    await process.wait()
    # 当子进程执行完毕时，拿到它的 stdout 属性
    stdout: StreamReader = process.stdout
    # 读取输出内容，如果子进程没有执行完毕，那么 await stdout.read() 会阻塞
    shell_result = (await stdout.read()).decode("utf-8")
    print(f"shell_result: \n{shell_result}")


asyncio.run(ls_print_in_control())
