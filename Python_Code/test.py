import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
from time import sleep


red_values = {}
green_values = {}

current_screen = "PlayerEntry"



root = tk.Tk()

screen_width = root.winfo_screenwidth() if root.winfo_screenwidth() < 1920 else 1920
screen_height = root.winfo_screenheight()

root.title("Edit Current Game")
root.geometry(f"{screen_width-10}x{screen_height-50}")
root.resizable(False, False)
root.configure(background="black")
root_label = tk.Label(root, text="Player Entry Screen", bg="black", height=4, width=40, bd=4, font=("Arial", 16, "bold"), fg="white")
root_label.pack()

frame = tk.Frame(root, width=400, height=200, bg="black")
frame.pack(expand=True, fill="both")

def countdown_timer(root: tk.Tk, reference_frame: tk.Frame, duration: int = 30) -> None:
    """Creates and starts a countdown timer inside the given frame."""
    timer_label = tk.Label(reference_frame, text=f"{duration} sec", font=("Monotone", 50), fg="white", bg="black")
    timer_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update_timer(time_left: int):
        if time_left > 0:
            timer_label.config(text=f"{time_left} sec")
            root.after(1000, lambda: update_timer(time_left - 1))
        else:
            timer_label.config(text="Finished", fg="red")

    update_timer(duration)  # Start the timer

countdown_timer(root, frame)

root.mainloop()
