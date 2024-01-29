import win32clipboard
from colorama import Fore, init
import keyboard
import os

init(autoreset=True)
cb = []

def get_data():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()    
    if data not in cb:
        cb.append(data)
    win32clipboard.CloseClipboard()
    
    os.system('cls')
    for i in range(len(cb)):
        print(f"{Fore.GREEN}{i}. {Fore.LIGHTBLUE_EX}{cb[i]}")

while True:
    keyboard.add_hotkey('tab', get_data)
    keyboard.wait()
