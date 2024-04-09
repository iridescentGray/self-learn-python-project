import time

from pynput.mouse import Button, Controller

mouse = Controller()  # Objects for manipulating the mouse


mouse.press(Button.left)  # 按住鼠标左键
mouse.release(Button.left)  # 松开左键
# 上面两行连在一起等于一次单击
time.sleep(1)

mouse.click(Button.right, 2)  # 当然鼠标点击我们有更合适的办法，使用click函数，右击两次
time.sleep(1)
