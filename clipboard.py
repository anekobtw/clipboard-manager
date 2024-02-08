import threading
import time
from tkinter import Tk

import customtkinter
import keyboard
import win32clipboard


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.is_shown = True

    def create_widgets(self):
        self.option_menu = customtkinter.CTkOptionMenu(self, values=cb)
        self.option_menu.pack(padx=5, pady=5)

        self.button = customtkinter.CTkButton(self, text='Insert', command=self.insert_text)
        self.button.pack(padx=5, pady=5)

    def update_option_menu(self):
        self.option_menu.configure(values=cb)

    def insert_text(self):
        text = self.option_menu.get()
        self.is_shown = False
        self.withdraw()
        keyboard.write(text)


def get_data(app: App):
    time.sleep(0.1)  # prevents a bug

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    if data not in cb:
        cb.append(data)
        app.update_option_menu()


def keyboard_listener1(app: App):
    while True:
        keyboard.wait('ctrl + c')
        get_data(app)


def keyboard_listener2(app: App):
    while True:
        keyboard.wait('win + v')
        if app.is_shown:
            app.withdraw()
            app.is_shown = False
        else:
            x, y = Tk().winfo_pointerxy()
            app.geometry(f'+{x}+{y}')
            app.deiconify()
            app.is_shown = True


if __name__ == '__main__':
    cb = []

    app = App()
    app.create_widgets()

    keyboard_thread1 = threading.Thread(target=keyboard_listener1, args=(app,), daemon=True)
    keyboard_thread1.start()

    keyboard_thread2 = threading.Thread(target=keyboard_listener2, args=(app,), daemon=True)
    keyboard_thread2.start()

    app.mainloop()

