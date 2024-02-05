import tkinter as tk
from tkinter import filedialog, scrolledtext

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True)
        self.text_widget.pack(expand=True, fill="both")

    def get_selected_text(self):
        return self.text_widget.get(tk.SEL_FIRST, tk.SEL_LAST)

    def delete_selected_text(self):
        self.text_widget.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def get_clipboard_text(self):
        return self.root.clipboard_get()

    def insert_text(self, text):
        self.text_widget.insert(tk.INSERT, text)

    def undo(self):
        try:
            self.text_widget.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text_widget.edit_redo()
        except tk.TclError:
            pass

    def show_find_dialog(self):
        return filedialog.askstring("Find", "Enter text to find:")

    def find_text(self, search_term):
        start_pos = self.text_widget.search(search_term, tk.SEL_LAST, stopindex=tk.END)
        if start_pos:
            self.text_widget.tag_remove(tk.SEL, "1.0", tk.END)
            self.text_widget.tag_add(tk.SEL, start_pos, f"{start_pos}+{len(search_term)}c")
            return start_pos
        return -1

    def select_text(self, start_index, length):
        end_index = f"{start_index}+{length}c"
        self.text_widget.tag_add(tk.SEL, start_index, end_index)

    def show_replace_dialog(self):
        search_term = filedialog.askstring("Replace", "Enter text to find:")
        replacement = filedialog.askstring("Replace", "Enter replacement text:")
        return search_term, replacement

    def replace_text(self, start_index, length, replacement):
        end_index = f"{start_index}+{length}c"
        self.text_widget.delete(start_index, end_index)
        self.text_widget.insert(start_index, replacement)


class EditingFunctions:
    def __init__(self, text_editor):
        self.text_editor = text_editor
        self.init_actions()

    def init_actions(self):
        self.text_editor.add_action('Cut', self.cut_text)
        self.text_editor.add_action('Copy', self.copy_text)
        self.text_editor.add_action('Paste', self.paste_text)
        self.text_editor.add_action('Undo', self.undo_text)
        self.text_editor.add_action('Redo', self.redo_text)
        self.text_editor.add_action('Find', self.find_text)
        self.text_editor.add_action('Replace', self.replace_text)

    def cut_text(self):
        selected_text = self.text_editor.get_selected_text()
        self.text_editor.delete_selected_text()
        self.text_editor.copy_to_clipboard(selected_text)

    def copy_text(self):
        selected_text = self.text_editor.get_selected_text()
        self.text_editor.copy_to_clipboard(selected_text)

    def paste_text(self):
        clipboard_text = self.text_editor.get_clipboard_text()
        self.text_editor.insert_text(clipboard_text)

    def undo_text(self):
        self.text_editor.undo()

    def redo_text(self):
        self.text_editor.redo()

    def find_text(self):
        search_term = self.text_editor.show_find_dialog()
        found_index = self.text_editor.find_text(search_term)
        if found_index != -1:
            self.text_editor.select_text(found_index, len(search_term))

    def replace_text(self):
        search_term, replacement = self.text_editor.show_replace_dialog()
        found_index = self.text_editor.find_text(search_term)
        if found_index != -1:
            self.text_editor.replace_text(found_index, len(search_term), replacement)


class EditorWidget(tk.Tk):
    def __init__(self):
        super().__init__()

        self.text_editor = TextEditor(self)
        self.editing_functions = EditingFunctions(self.text_editor)

        self.init_ui()

    def init_ui(self):
        self.title("Text Editor")

        # Create a menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create a file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # Add actions to the file menu
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_editor.text_widget.get("1.0", tk.END))

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_editor.text_widget.delete("1.0", tk.END)
                self.text_editor.text_widget.insert(tk.END, content)

if __name__ == "__main__":
    app = EditorWidget()
    app.mainloop()
