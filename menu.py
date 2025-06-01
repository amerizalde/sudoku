import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self, root):
        self.root = root
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Rules of Sudoku", command=self.show_rules)

    def show_rules(self):
        rules_text = (
            "Sudoku Rules:\n"
            "1. Each row must contain the numbers 1-9 without repetition.\n"
            "2. Each column must contain the numbers 1-9 without repetition.\n"
            "3. Each of the nine 3x3 subgrids must contain the numbers 1-9 without repetition."
        )
        messagebox.showinfo("Rules of Sudoku", rules_text)
