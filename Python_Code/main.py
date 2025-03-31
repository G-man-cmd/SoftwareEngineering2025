import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
from time import sleep


red_values = {}
green_values = {}



current_screen = "PlayerEntry"



root = tk.Tk()

screen_width = (root.winfo_screenwidth() if root.winfo_screenwidth() < 1920 else 1920)-10
screen_height = (root.winfo_screenheight() if root.winfo_screenheight() < 1080 else 1080 )-10

img = Image.open("logo.jpg")
img = img.resize((screen_width,screen_height))
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image = photo)
label.pack()

root.after(3000, label.destroy)

network_address = tk.StringVar()
broadcast_port = tk.StringVar()
recv_port = 7501


root.title("Edit Current Game")
root.geometry(f"{screen_width-10}x{screen_height-60}")
root.resizable(False, False)
root.configure(background="black")
root_label = tk.Label(root, text="Player Entry Screen", bg="black", height=4, width=40, bd=4, font=("Arial", 16, "bold"), fg="white")
root_label.pack()

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
red_box_label.grid(row=1, column=0, columnspan=10, pady=5)


green_box_label = tk.Label(green_base, text="Name                            Hardware ID", font=("Arial", 12), bg="green", fg="white")
green_box_label.grid(row=1, column=0, columnspan=10, pady=5)


def network_frame():
    global network_frame
    network_frame = tk.Frame(root,height=150,width=280,bg='black')
    network_frame.place(x=1550,y=250)

    widget_label = tk.Label(network_frame, text = 'Network Interface', font=('calibre',12, 'bold'),fg="red",bg="black")
    widget_label.grid(row=0,column=1,padx=2)

    add_label = tk.Label(network_frame, text = 'Address: ', font=('calibre',10),fg="white",bg="black")
    add_label.grid(row=1,column=0)
    add_entry = tk.Entry(network_frame, font=('calibre',10,'normal'),textvariable=network_address)
    add_entry.insert(0,"127.0.0.1")
    add_entry.grid(row=1,column=1)

    port_label = tk.Label(network_frame, text = 'Broadcast Port: ', font = ('calibre',10),fg="white",bg="black")
    port_label.grid(row=2,column=0)
    port_entry=tk.Entry(network_frame, font = ('calibre',10,'normal'),textvariable=broadcast_port)
    port_entry.grid(row=2,column=1)
    port_entry.insert(0,"7500")
 



def create_entry_grid(red_frame,green_frame):
    root.after(3000,network_frame)

    for row in range(2,22):  #20 rows
        red_details = [tk.StringVar(),tk.StringVar()]
        red_values[row-1] = red_details

        green_details = [tk.StringVar(),tk.StringVar()]
        green_values[row-1] = green_details

        red_label = tk.Label(red_frame,text=row-1,font=('calibre',10),fg='black',bg='red')
        red_label.grid(row=row+1,column=0)

        red_entry = tk.Entry(red_frame, width=20, textvariable=red_details[0])
        red_entry.grid(row=row+1, column=1, padx=5, pady=4, sticky="ew")
        red_entry = tk.Entry(red_frame, width=20, textvariable=red_details[1])
        red_entry.grid(row=row+1, column=2, padx=5, pady=4, sticky="ew")

        green_label = tk.Label(green_frame,text=row-1,font=('calibre',10),fg='black',bg='green')
        green_label.grid(row=row+1,column=0)

        green_entry = tk.Entry(green_frame, width=20, textvariable=green_details[0])
        green_entry.grid(row=row+1, column=1, padx=5, pady=4, sticky="ew")
        green_entry = tk.Entry(green_frame, width=20, textvariable=green_details[1])
        green_entry.grid(row=row+1, column=2, padx=5, pady=4, sticky="ew")

create_entry_grid(red_base,green_base)




def countdown_timer(root: tk.Tk, reference_frame: tk.Frame, duration: int = 30) -> None:
    timer_label = tk.Label(reference_frame, text=f"{duration} sec", font=("Monotone", 50), fg="white", bg="black")
    timer_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update_timer(time_left: int):
        if time_left > 0:
            timer_label.config(text=f"{time_left} sec")
            root.after(1000, lambda: update_timer(time_left - 1))
        else:
            timer_label.config(text="Finished", fg="red")

    update_timer(duration)

def editGame():
    pass
def gameParameters():
    unwrap_entries()
def startGame():
    current_screen = "Live"
    countdown_timer(root,timer_canvas)


def preEnteredGames():
    network_frame.destroy()
    unwrap_entries()
    root_label.config(text="Live Events")
    if current_screen == "PlayerEntry":
        base.grid_forget()
        base.destroy()

        live_base = tk.Frame(root,height=400,width=1000,bg='white')
        live_base.pack()

        red_live = tk.Frame(live_base,height=400,width=500,bg='red',padx=30, pady=0)
        red_live.pack(side='left')

        red_live_tree = ttk.Treeview(red_live, selectmode ='browse',height=15)
        red_live_tree.pack(side ='right',anchor='s',pady=50)

        red_live_tree["columns"] = ("1", "2", "3")
        red_live_tree["show"] = 'headings'

        red_live_tree.column("1", width = 165, anchor ='c')
        red_live_tree.column("2", width = 90, anchor ='se')
        red_live_tree.column("3", width = 165, anchor ='se')

        verscrlbar = ttk.Scrollbar(red_live, 
                           orient ="vertical", 
                           command = red_live_tree.yview)
        verscrlbar.pack(side ='right', fill ='x')
        red_live_tree.configure(xscrollcommand = verscrlbar.set)

        red_live_tree.heading("1", text ="Name")
        red_live_tree.heading("2", text ="H_ID")
        red_live_tree.heading("3", text ="Score")

        label_red = tk.Label(red_live, text="RED TEAM", font=("Arial", 14, "bold"), bg="red", fg="white")
        label_red.place(relx=0.5, rely=0.05, anchor="center")

        label_red_total = tk.Label(red_live, text="Total Score: 0", font=("Arial", 14, "bold"), bg="red", fg="white")
        label_red_total.place(x=300,y=380)


        green_live = tk.Frame(live_base,height=400,width=500,bg='green',padx=30, pady=0)
        green_live.pack(side='right')
        green_live.grid_propagate(0)
        
        green_live_tree = ttk.Treeview(green_live, selectmode ='browse',height=15)
        green_live_tree.pack(side ='right',anchor='s',pady=50)

        green_live_tree["columns"] = ("1", "2", "3")
        green_live_tree["show"] = 'headings'

        green_live_tree.column("1", width = 165, anchor ='c')
        green_live_tree.column("2", width = 90, anchor ='se')
        green_live_tree.column("3", width = 165, anchor ='se')

        verscrlbar = ttk.Scrollbar(green_live, 
                           orient ="vertical", 
                           command = green_live_tree.yview)
        verscrlbar.pack(side ='right', fill ='x')
        red_live_tree.configure(xscrollcommand = verscrlbar.set)

        green_live_tree.heading("1", text ="Name")
        green_live_tree.heading("2", text ="H_ID")
        green_live_tree.heading("3", text ="Score")

        label_green = tk.Label(green_live, text="GREEN TEAM", font=("Arial", 14, "bold"), bg="green", fg="white")
        label_green.place(relx=0.5, rely=0.05, anchor="center")

        label_green_total = tk.Label(green_live, text="Total Score: 0", font=("Arial", 14, "bold"), bg="green", fg="white")
        label_green_total.place(x=300,y=380)


        for i in red_values.keys():
            name = (red_values[i])[0]
            h_id = (red_values[i])[1]
            if len(name) > 0:
                red_live_tree.insert("", 'end', text ="L1", values =(name, h_id, "0"))


        for i in green_values.keys():
            name = (green_values[i])[0]
            h_id = (green_values[i])[1]
            if len(name) > 0:
                green_live_tree.insert("", 'end', text ="L1", values =(name, h_id, "0"))
        


        event_live_scroll = tk.Frame(root,height=400,width=1000,bg='white')
        event_live_scroll.pack()

        sf = ScrolledFrame(event_live_scroll,height=500,width=980)
        sf.pack(side="top", expand=1, fill="both",pady=30)
        scroll_frame = sf.display_widget(tk.Frame)
        label_live = tk.Label(event_live_scroll, text="Live Events", font=("Arial", 12,), fg="black", bg="white")
        label_live.place(relx=0.5, rely=0.08, anchor="center")

        global timer_canvas
        timer_canvas = tk.Frame(root,height=150,width=280,bg='black')
        timer_canvas.place(x=1550,y=450)
    
network_address = network_address.get()
broadcast_port = broadcast_port.get()


def viewGame():
    unwrap_entries()

    print(red_values)

    print("===")

    print(green_values)

def flickSync():
    pass

def clearGame():
    if current_screen == "PlayerEntry":
        create_entry_grid(red_base)
        create_entry_grid(green_base)


def unwrap_entries():
    if current_screen == "PlayerEntry":
        for i in red_values.keys():
            values = []
            for j in red_values[i]:
                values.append(j.get())
            red_values[i]=values
        
        for i in green_values.keys():
            values = []
            for j in green_values[i]:
                values.append(j.get())
            green_values[i]=values



buttonFrame = tk.Frame(root,bg="black")
buttonFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=20,padx=650)
f1 = tk.Button(buttonFrame, text = "F1\n Edit \n Game", bg = "black", fg = "green", command=editGame)
f1.grid(row=0,column=0)
f2 = tk.Button(buttonFrame, text = "F2\nGame \nParameters", bg = "black", fg = "green", command=gameParameters)  
f2.grid(row=0,column=1)
f3 = tk.Button(buttonFrame, text = "F3\nPregame\nTimer", bg = "black", fg = "green", command=startGame)
f3.grid(row=0,column=2)
f5 = tk.Button(buttonFrame, text = "F5\nPregame\n Screen", bg = "black", fg = "green", command=preEnteredGames)
f5.grid(row=0,column=3)
f8 = tk.Button(buttonFrame, text = "F8\nView \nGame", bg = "black", fg = "green", command=viewGame)
f8.grid(row=0,column=4)
f10 = tk.Button(buttonFrame, text = "F10\nFlick \nSync", bg = "black", fg = "green", command=flickSync)
f10.grid(row=0,column=5)
f12 = tk.Button(buttonFrame, text = "F12\nClear \nGame", bg = "black", fg = "green", command=clearGame)
f12.grid(row=0,column=6)

root.bind("<F1>", lambda event: editGame())
root.bind("<F2>", lambda event: gameParameters())
root.bind("<F3>", lambda event: startGame())
root.bind("<F5>", lambda event: preEnteredGames())
root.bind("<F8>", lambda event: viewGame())
root.bind("<F10>", lambda event: flickSync())
root.bind("<F12>", lambda event: clearGame())
root.bind("<Escape>", lambda event: root.quit())


root.mainloop()
