import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from editing_functions import EditingFunctions
from syntax_highlighting import CodeEditorHighlighter

class EditorWidget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill='both')
        self.create_widgets()

    def create_widgets(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)


def main():
    root = tk.Tk()
    root.title("Code Editor")
    root.geometry("800x600")

    editor_widget = EditorWidget(root)

    root.mainloop()

if __name__ == "__main__":
    main()
