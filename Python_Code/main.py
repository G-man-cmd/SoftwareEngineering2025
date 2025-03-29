from typing import Dict, List
from tkinter import Tk, Label
from PIL import Image, ImageTk
import tkinter as tk
#import psycopg2
#from psycog2 import sql
import os
from Python_Code.player_data import Player


#from network import Network
#from database import Database
#import action_screen
#import player_entry

def main():
    players: Dict[str, List[Player]] = {
        "red": [],
        "green": []
    }

    #establish way to talk to network.

    #splash screen goes here
    root = Tk()
    root.title("Splash Screen")

    img = Image.open("Python_Code/logo.jpg")
    img = img.resize((1600, 1000))
    photo = ImageTk.PhotoImage(img)

    label = Label(root, image = photo)
    label.pack()

    root.after(3000, root.destroy)

    #call player entry

    #call action screen after entry

    root.mainloop()
if __name__ == "__main__":
    main()