import asyncio
from asyncio import Transport, AbstractEventLoop
from typing import Optional

"""
传输和协议是较低级别的 API，最适合在发送和接收数据时直接控制所发生的事情。
例如，如果正在设计一个网络库或 Web 框架，可能会考虑传输和协议。
但对于大多数应用程序，我们不需要这种级别的控制.去使用高级的API Stream吧
"""


class HTTPGetClientProtocol(asyncio.Protocol):

    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host = host
        self._future = loop.create_future()
        self._transport: Optional[Transport] = None
        self._response_buffer: bytes = b""

    async def get_response(self):
        # 等待 self._future，直到从服务器得到响应并写入 self._future
        return await self._future

    def _get_request_bytes(self) -> bytes:
        request = ("GET / HTTP/1.1\r\n"
                   "Connection: close\r\n"
                   f"Host: {self._host}\r\n\r\n")
        return request.encode("utf-8")

    def connection_made(self, transport: Transport) -> None:
        """底层套接字和服务器端建立连接时会调用此方法"""
        print(f"和 {self._host} 建立连接")
        # 会自动传入一个 transport 参数，它就是传输，我们用它来管理数据
        # 并在事件发生时调用协议上的方法，比如这里的 connection_made，我们将传输保存起来
        self._transport = transport
        # 调用传输的 write 方法写入数据
        self._transport.write(self._get_request_bytes())

    def data_received(self, data: bytes) -> None:
        """传输在收到数据时会调用协议的 data_received 方法"""
        print("收到数据")
        self._response_buffer += data

    def eof_received(self) -> Optional[bool]:
        """
        如果服务端已经将所有数据都返回完毕，那么会关闭连接
        此时传输会自动调用协议的 eof_received 方法
        """
        print("数据全部接收完毕")
        # 响应数据都接收完毕，将其写入 future 中
        self._future.set_result(self._response_buffer)
        # 该方法返回一个布尔值，用于确定如何关闭传输（底层套接字）
        # 返回 False 则让传输自行关闭，返回 True 意味着需要编写协议来关闭
        # 由于当前不需要在关闭时执行什么特殊逻辑，所以返回 False 即可
        # 因此我们不需要手动处理关闭传输
        return False

    def connection_lost(self, exc: Optional[Exception]) -> None:
        """当连接关闭时会调用此方法"""
        # 如果连接正常关闭，则什么也不做
        if exc is None:
            print("连接正常关闭")
        else:
            # 否则将异常设置到 future 里面
            self._future.set_exception(exc)


async def make_request(host: str, port: int, loop: AbstractEventLoop):
    # 协议工厂，调用之后创建一个协议实例
    def protocol_factory():
        return HTTPGetClientProtocol(host, loop)

    # create_connection 将创建到给定主机的套接字连接，并将其包装在适当的传输中
    # 当建立连接之后，会自动调用协议的 connection_made，在该方法中会向目的主机发送请求
    # 当数据达到时，会自动协议的 data_received，数据返回完毕时自动调用协议的 eof_received
    transport, protocol = await loop.create_connection(protocol_factory, host=host, port=port)
    # 将数据写入 future 之后，调用 get_response 得到响应数据
    # 在 create_connection 里面我们传入了一个协议工厂，在里面会自动调用
    # 返回的 transport 就是传输，protocol 就是内部的创建协议实例，但传输这里我们不需要
    return await protocol.get_response()


async def main():
    loop = asyncio.get_running_loop()
    result = await make_request("www.baidu.com", 80, loop)
    print("百度一下".encode("utf-8") in result)


asyncio.run(main())
