import time

from pynput.mouse import Controller

if __name__ == "__main__":
    mouse = Controller()
    while True:
        mouse.move(0.5, 0.5)
        time.sleep(10)
        mouse.move(-0.5, -0.5)
        time.sleep(10)
