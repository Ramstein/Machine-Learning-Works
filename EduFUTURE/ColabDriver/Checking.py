import pyperclip
import pyautogui

scriptPath = r'C:\Users\Ramstein\PycharmProjects\Keras\Recognizing Handwritten Digits.py'


with open(scriptPath) as f:
    lines = f.readlines()
    for line in lines:
        pyperclip.copy(line)
        fromClipboard = pyautogui.hotkey('ctrl', 'v')
        print(fromClipboard, '\b')


        '/html/body/div/span[2]/pre/a'

