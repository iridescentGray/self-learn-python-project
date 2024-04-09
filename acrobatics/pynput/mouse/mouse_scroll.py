import time

from pynput.mouse import Controller

mouse = Controller()  # Objects for manipulating the mouse
time.sleep(1)
mouse.scroll(500, 500)  # scroll mouse
