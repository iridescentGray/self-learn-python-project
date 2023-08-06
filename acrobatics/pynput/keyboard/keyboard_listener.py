from pynput.keyboard import Key, Listener


def on_press(key):
    # 当按下esc，结束监听
    if key == Key.esc:
        print(f"你按下了esc，监听结束")
        return False
    print(f"你按下了{key.char if hasattr(key, 'char') else key.name}键")


def on_release(key):
    print(f"你松开了{key.char if hasattr(key, 'char') else key.name}键")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
