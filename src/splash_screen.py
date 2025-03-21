from PIL import Image, ImageTk
import tkinter as tk

# Build the splash screen, destroy after 3 seconds
def build(root: tk.Tk) -> tk.Label:
    # Load the splash screen image
    image: Image = Image.open("assets/backgrounds/logo.jpg")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    image = image.resize((width, height))

    splash_image: ImageTk.PhotoImage = ImageTk.PhotoImage(image)

    # Build the splash screen
    splash_screen: tk.Label = tk.Label(root, image=splash_image)
    splash_screen.place(x=0, y=0, relwidth=1, relheight=1)
    splash_screen.image: ImageTk.PhotoImage = splash_image

    # Make background black
    splash_screen.configure(background="black")
    return splash_screen