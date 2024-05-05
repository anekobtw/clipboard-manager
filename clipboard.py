import threading
import time
from tkinter import Tk

import customtkinter
import keyboard
import pyperclip

VERSION = "1.0.1"


class ClipboardManagerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"Clipboard Manager {VERSION}")
        self.clipboard = []
        self.create_widgets()

    def create_widgets(self) -> None:
        self.option_menu = customtkinter.CTkOptionMenu(
            self,
            variable=customtkinter.StringVar(self, value="Clipboard is empty"),
            values=self.clipboard,
            state="disabled",
        )
        self.option_menu.pack(padx=5, pady=5)

        self.insert_button = customtkinter.CTkButton(self, text="Insert", fg_color="green", command=self.insert_text)
        self.insert_button.pack(padx=5, pady=5)

        self.insert_button = customtkinter.CTkButton(self, text="Delete", fg_color="red", command=self.delete_text)
        self.insert_button.pack(padx=5, pady=5)

    def update_option_menu(self) -> None:
        if self.clipboard:
            self.option_menu.configure(variable=customtkinter.StringVar(self, value="Choose an option"), values=self.clipboard)
        else:
            self.option_menu.configure(variable=customtkinter.StringVar(self, value="Clipboard is empty"), values=self.clipboard)
        self.option_menu.configure(state="enabled") if self.clipboard else self.option_menu.configure(state="disabled")

    def insert_text(self) -> None:
        if self.option_menu._state == "enabled":
            self.withdraw()
            keyboard.write(self.option_menu.get())
        else:
            self.withdraw()

    def delete_text(self) -> None:
        self.clipboard.remove(self.option_menu.get())
        self.update_option_menu()
        self.withdraw()


def get_clipboard_data(app: ClipboardManagerApp) -> None:
    time.sleep(0.1)  # prevents a bug

    try:
        data = pyperclip.paste()
        if data and data not in app.clipboard:
            app.clipboard.append(data)
            app.update_option_menu()
    except pyperclip.PyperclipException as e:
        print(f"Error getting clipboard data: {e}")


def keyboard_listener1(app: ClipboardManagerApp) -> None:
    while True:
        keyboard.wait("ctrl + c")
        get_clipboard_data(app)


def keyboard_listener2(app: ClipboardManagerApp) -> None:
    while True:
        keyboard.wait("win + v")
        if app.state() == "withdrawn":
            x, y = Tk().winfo_pointerxy()
            app.deiconify()
            app.geometry(f"+{x}+{y}")
        else:
            app.withdraw()


if __name__ == "__main__":
    app = ClipboardManagerApp()

    keyboard_thread1 = threading.Thread(target=keyboard_listener1, args=(app,), daemon=True)
    keyboard_thread1.start()

    keyboard_thread2 = threading.Thread(target=keyboard_listener2, args=(app,), daemon=True)
    keyboard_thread2.start()

    app.mainloop()
