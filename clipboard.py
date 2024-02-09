import threading
import time
from tkinter import Tk
from typing import NoReturn

import customtkinter
import keyboard
import pyperclip


class ClipboardManagerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Clipboard Manager')
        self.clipboard = []
        self.create_widgets()

    def create_widgets(self) -> None:
        self.option_menu = customtkinter.CTkOptionMenu(self, values=self.clipboard)
        self.option_menu.pack(padx=5, pady=5)

        self.insert_button = customtkinter.CTkButton(self, text='Insert', command=self.insert_text)
        self.insert_button.pack(padx=5, pady=5)

    def update_option_menu(self) -> None:
        self.option_menu.configure(values=self.clipboard)

    def insert_text(self) -> None:
        text = self.option_menu.get()
        self.withdraw()
        keyboard.write(text)


def get_clipboard_data(app: ClipboardManagerApp) -> None:
    time.sleep(0.1)  # prevents a bug

    try:
        data = pyperclip.paste()
        if data and data not in app.clipboard:
            app.clipboard.append(data)
            app.update_option_menu()
    except pyperclip.PyperclipException as e:
        print(f"Error getting clipboard data: {e}")


def keyboard_listener1(app: ClipboardManagerApp) -> NoReturn:
    while True:
        keyboard.wait('ctrl + c')
        get_clipboard_data(app)


def keyboard_listener2(app: ClipboardManagerApp) -> NoReturn:
    while True:
        keyboard.wait('win + v')
        if app.state() == "withdrawn":
            x, y = Tk().winfo_pointerxy()
            app.deiconify()
            app.geometry(f'+{x}+{y}')
        else:
            app.withdraw()


if __name__ == '__main__':
    app = ClipboardManagerApp()

    keyboard_thread1 = threading.Thread(target=keyboard_listener1, args=(app,), daemon=True)
    keyboard_thread1.start()

    keyboard_thread2 = threading.Thread(target=keyboard_listener2, args=(app,), daemon=True)
    keyboard_thread2.start()

    app.mainloop()
