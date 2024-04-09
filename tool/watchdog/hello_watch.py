import os

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class CodeEventHandler(FileSystemEventHandler):
    def on_moved(self, event):
        print(f"{event.src_path} 被重命名了")

    def on_created(self, event):
        print(f"{event.src_path}被创建了")

    def on_deleted(self, event):
        print(f"{event.src_path}被删除了")

    def on_modified(self, event):
        print(f"{event.src_path}被修改了")


def main():
    observer = Observer()
    watch_path = os.path.dirname(os.path.abspath(__file__))  # watch current file dir
    observer.schedule(CodeEventHandler(), watch_path, True)
    observer.start()  # 启了一个守护线程启动监听,若程序结束, 该线程也会停止
    while True:
        ...


main()
