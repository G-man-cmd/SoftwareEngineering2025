import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import action_screen.game_screen as game_screen

root = tk.Tk()

screen_width = root.winfo_screenwidth() if root.winfo_screenwidth() < 1920 else 1920
screen_height = root.winfo_screenheight()

img = Image.open("logo.jpg")
img = img.resize((screen_width,screen_height))
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image = photo)
label.pack()

root.after(3000, label.destroy)


root.title("Edit Current Game")
root.geometry(f"{screen_width-10}x{screen_height-50}")
root.resizable(False, False)
root.configure(background="black")
tk.Label(root, text="Payer Entry Screen", bg="black", height=4, width=40, bd=4, font=("Arial", 16, "bold"), fg="white").pack()

base = tk.Frame(root,height=700,width=1000,bg='white')
base.pack()
base.grid_propagate(0)

red_base = tk.Frame(base,height=700,width=500,bg='red',padx=30, pady=0)
red_base.pack(side='left')
red_base.grid_propagate(0)
label_red = tk.Label(red_base, text="RED TEAM", font=("Arial", 14, "bold"), bg="red", fg="white")
label_red.grid(row=0, column=0, columnspan=10, pady=5)

green_base = tk.Frame(base,height=700,width=500,bg='green',padx=30, pady=0)
green_base.pack(side='right')
green_base.grid_propagate(0)
label_green = tk.Label(green_base, text="GREEN TEAM", font=("Arial", 14, "bold"), bg="green", fg="white")
label_green.grid(row=0, column=0, columnspan=10, pady=5)


red_box_label = tk.Label(red_base, text="Name                            Hardware ID", font=("Arial", 12), bg="red", fg="white")
red_box_label.grid(row=1, column=1, columnspan=10, pady=5)


green_box_label = tk.Label(green_base, text="Name                            Hardware ID", font=("Arial", 12), bg="green", fg="white")
green_box_label.grid(row=1, column=1, columnspan=10, pady=5)




def create_entry_grid(parent_frame):
    entries = []  # Store entries if needed later
    for row in range(2,22):  # 20 rows
        row_entries = []
        label = tk.Label(parent_frame,text=f"{row-1}",height=1,width=2)
        label.grid(row=row, column=0)
        for col in range(2):  # 2 columns
            entry = tk.Entry(parent_frame, width=25)  # Small width for compact layout
            entry.grid(row=row, column=col+1, padx=1, pady=3,sticky="ew")
            row_entries.append(entry)
        entries.append(row_entries)

create_entry_grid(red_base)
create_entry_grid(green_base)

def editGame():
    pass
def gameParameters():
    pass
def startGame():
    game = game_screen(players)
    game.create_game_action_screen(root, main_frame, None, None, None, None)
    action_screen = tk.Frame(root, bg = "black",height=500,width=500)






def preEnteredGames():
    pass
def viewGame():
    pass
def flickSync():
    pass
def clearGame():
    create_entry_grid(red_base)
    create_entry_grid(green_base)


root.bind("<Escape>", lambda event: root.quit())


buttonFrame = tk.Frame(root, bg="black")
buttonFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)
f1 = tk.Button(buttonFrame, text = "F1\n Edit \n Game", bg = "black", fg = "green", command=editGame)
f1.pack(side = tk.LEFT, padx=20)
f2 = tk.Button(buttonFrame, text = "F2\nGame \nParameters", bg = "black", fg = "green", command=gameParameters)  
f2.pack(side = tk.LEFT, padx=20)
f3 = tk.Button(buttonFrame, text = "F3\nStart \nGame", bg = "black", fg = "green", command=startGame)
f3.pack(side = tk.LEFT, padx=20)
f4 = tk.Button(buttonFrame, text = "", bg = "black", fg = "black")
f4.pack(side = tk.LEFT, padx=20)
f5 = tk.Button(buttonFrame, text = "F5\nPreEntered\n Games", bg = "black", fg = "green", command=preEnteredGames)
f5.pack(side = tk.LEFT, padx=20)
f6 = tk.Button(buttonFrame, text = "", bg = "black", fg = "black")
f6.pack(side = tk.LEFT, padx=20)
f7 = tk.Button(buttonFrame, text = "F7\n", bg = "black", fg = "green")
f7.pack(side = tk.LEFT, padx=20)
f8 = tk.Button(buttonFrame, text = "F8\nView \nGame", bg = "black", fg = "green", command=viewGame)
f8.pack(side = tk.LEFT, padx=20)
f9 = tk.Button(buttonFrame, text = "", bg = "black", fg = "black")
f9.pack(side = tk.LEFT, padx=20)
f10 = tk.Button(buttonFrame, text = "F10\nFlick \nSync", bg = "black", fg = "green", command=flickSync)
f10.pack(side = tk.LEFT, padx=20)
f11 = tk.Button(buttonFrame, text = "", bg = "black", fg = "black")
f11.pack(side = tk.LEFT, padx=20)
f12 = tk.Button(buttonFrame, text = "F12\nClear \nGame", bg = "black", fg = "green", command=clearGame)
f12.pack(side = tk.LEFT, padx=20)

root.bind("<F1>", lambda event: editGame())
root.bind("<F2>", lambda event: gameParameters())
root.bind("<F3>", lambda event: startGame())
root.bind("<F5>", lambda event: preEnteredGames())
root.bind("<F8>", lambda event: viewGame())
root.bind("<F10>", lambda event: flickSync())
root.bind("<F12>", lambda event: clearGame())






root.mainloop()
