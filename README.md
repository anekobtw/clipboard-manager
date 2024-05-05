# Clipboard Manager
The Clipboard Manager is a Python application designed to enhance clipboard management on your system. It provides a user-friendly interface along with convenient keyboard shortcuts for efficient handling of clipboard content.

## Features
- Clipboard Monitoring: The application monitors the system clipboard for changes and automatically updates the clipboard history.
- Insert Text: Users can insert text from the clipboard history into any active text field with a single click.
- Delete Text: Unwanted items in the clipboard history can be removed with the delete function.
- Minimalist GUI: The user interface is clean and intuitive, providing easy access to clipboard history.

## Quick start
1. Clone the repository:
```
$ git clone https://github.com/anekobtw/clipboard-manager.git
```

2. Install dependencies:
```
$ pip install -r requirements.txt
```

3. Run the application
```
$ python clipboard.py
```

4. Press Ctrl + C to capture text copied to the clipboard.
5. Press Win + V to toggle the visibility of the Clipboard Manager window.
6. Use the "Insert" button to insert selected text from the clipboard history.
7. Use the "Delete" button to remove selected text from the clipboard history.

## Acknowledgements
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) - A modern and customizable python UI-library based on Tkinter 
- [keyboard](https://github.com/boppreh/keyboard) - Hook and simulate global keyboard events on Windows and Linux.
- [pyperclip](https://github.com/asweigart/pyperclip) - Python module for cross-platform clipboard functions.

## Contributing
Contributions are always welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue on the [GitHub repository](https://github.com/anekobtw/clipboard-manager).

## Licence
Copyright © 2024 anekobtw.\
This project is [MIT](https://github.com/anekobtw/clipboard-manager/blob/main/LICENSE) licensed.
