from threading import Thread
import threading
from pynput.mouse import Listener, Button


def on_move(x, y):
    print(f"鼠标移动到: ({x}, {y})")


def on_click(x, y, button, is_press):
    if button == Button.right:
        print("点击右键，停止监控")
        return False  # 一旦当某个事件返回了False，那么就会停止了
    print(f"鼠标{button}键在({x}, {y})处{'按下' if is_press else '松开'}")


def on_scroll(x, y, dx, dy):
    if dx:
        print(f"滑轮在({x}, {y})处向{'右' if dx > 0 else '左'}滑")
    else:
        print(f"滑轮在({x}, {y})处向{'下' if dy > 0 else '上'}滑")


def run_listener():
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()


t = threading.Thread(target=run_listener, name="LoopThread")
t.start()
t.join()
