from tkinter import simpledialog

class EditingFunctions:
    def __init__(self, text_editor):
        self.text_editor = text_editor
        self.init_actions()

    def init_actions(self):
        self.text_editor.add_menu_commands([
            ('Cut', self.cut_text),
            ('Copy', self.copy_text),
            ('Paste', self.paste_text),
            ('Undo', self.undo_text),
            ('Redo', self.redo_text),
            ('Find', self.find_text),
            ('Replace', self.replace_text)
        ])

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
