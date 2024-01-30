import win32clipboard
from colorama import Fore, init
import keyboard
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
print(f'{Fore.YELLOW}Clipboard history is empty yet.')
init(autoreset=True)
cb = []


def get_data():
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    if data not in cb:
        cb.append(data)
    win32clipboard.CloseClipboard()

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(len(cb)):
        print(f"{Fore.GREEN}{i}. {Fore.LIGHTBLUE_EX}{cb[i]}")


while True:
    keyboard.add_hotkey('ctrl + c', get_data)
    keyboard.wait()
