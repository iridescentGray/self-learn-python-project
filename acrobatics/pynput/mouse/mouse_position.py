import time

from pynput.mouse import Controller

mouse = Controller()  # Objects for manipulating the mouse
print(f"当前鼠标位置: {mouse.position}")

mouse.position = (100, 100)  # equal mouse.move(100, 100)
time.sleep(1)

print(f"移动后的当前鼠标位置: {mouse.position}")  # 当前鼠标位置: (100, 100)
time.sleep(1)
