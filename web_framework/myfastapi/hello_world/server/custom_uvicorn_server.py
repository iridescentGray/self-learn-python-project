import contextlib
import threading
import time
from fastapi import APIRouter, FastAPI
import uvicorn


class UvicornServer(uvicorn.Server):
    """
    Multithreaded server - as found in https://github.com/encode/uvicorn/issues/742

    Removed install_signal_handlers() override based on changes from this commit:
        https://github.com/encode/uvicorn/commit/ce2ef45a9109df8eae038c0ec323eb63d644cbc6

    Cannot rely on asyncio.get_event_loop() to create new event loop because of this check:
        https://github.com/python/cpython/blob/4d7f11e05731f67fd2c07ec2972c6cb9861d52be/Lib/asyncio/events.py#L638

    Fix by overriding run() and forcing creation of new event loop if uvloop is available
    """

    def run(self, sockets=None):
        import asyncio

        """
        Parent implementation calls self.config.setup_event_loop(),
            but we need to create uvloop event loop manually
        """
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # When running in a thread, we'll not have an eventloop yet.
            loop = asyncio.new_event_loop()
        loop.run_until_complete(self.serve(sockets=sockets))

    @contextlib.contextmanager  # type: ignore
    def run_in_thread(self):
        self.thread = threading.Thread(target=self.run, name="FTUvicorn")
        self.thread.start()
        while not self.started:
            time.sleep(1e-3)

    def cleanup(self):
        self.should_exit = True
        self.thread.join()


"""Response
https://fastapi.tiangolo.com/zh/advanced/custom-response/

like chatgpt response

"""

router_public = APIRouter()


@router_public.get("/list")
async def index1():
    """
    http://127.0.0.1:5555/api/list  success

    """
    return [{"name": "test", "age": 17}, {"name": "test2", "age": 16}]


if __name__ == "__main__":
    app = FastAPI(
        title="custom_server",
        redoc_url=None,
    )
    app.include_router(router_public, prefix="/api")

    uvconfig = uvicorn.Config(
        app,
        port=5555,
        host="0.0.0.0",
        use_colors=False,
        log_config=None,
        access_log=True,
        ws_ping_interval=None,  # We do this explicitly ourselves
    )
    UvicornServer(uvconfig).run_in_thread()
