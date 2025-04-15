import tkinter as tk
from tkinter import scrolledtext

class ScrollableTextFrame:
    def __init__(self, root):
        self.root = root
        
        self.canvas = tk.Canvas(root, height=300, width=980, bg="white")
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.frame_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.text_labels = []
    
    def clear_all_text(self):
        for label in self.text_labels:
            label.destroy()
        self.text_labels.clear()
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(0.0)

    def add_text(self, new_text):
        label = tk.Label(self.scrollable_frame, text=new_text, bg="white", fg="black", anchor="w", justify="left")
        label.pack(fill="x", padx=3, pady=2)

        self.text_labels.insert(0, label)

        if len(self.text_labels) > 20:
            self.text_labels[-1].destroy()
            self.text_labels.pop()

        self.canvas.update_idletasks()
        self.canvas.yview_moveto(0.0)
