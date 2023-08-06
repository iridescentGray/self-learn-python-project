from curses import A_ALTCHARSET
import time
from pynput.keyboard import Key, Controller

keyboard: Controller = Controller()


keyboard.press("a")
keyboard.release("a")
time.sleep(1)

keyboard.press("A")
keyboard.release("A")
time.sleep(1)


keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)

# 组合键位,cmd+b 收起侧边栏
with keyboard.pressed(Key.cmd):
    keyboard.press("b")
