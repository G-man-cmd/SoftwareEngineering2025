from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()
root.title("Splash Screen")

img = Image.open("logo.jpg")
img = img.resize((1600, 1000))
photo = ImageTk.PhotoImage(img)

label = Label(root, image = photo)
label.pack()

root.after(3000, root.destroy)

root.mainloop()