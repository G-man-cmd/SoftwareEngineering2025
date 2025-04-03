import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
from time import sleep
from tkinter import messagebox
from database import Database
from server import Server
from scrollframe import ScrollableTextFrame
from music import RandomTrackPlayer
from current_game import CurrentGame,Player

pregame_timer = 5
game_timer =15

red_values = {}
green_values = {}

red_widget_dict = {}
green_widget_dict = {}

track_list=["Track01.mp3","Track03.mp3","Track05.mp3" ,"Track07.mp3","Track02.mp3","Track04.mp3","Track06.mp3","Track08.mp3"]

photon_player = RandomTrackPlayer(track_list)

current_screen = "PlayerEntry"

this_game = CurrentGame()

photon_db = Database(dbname='photon')


splash_screen_duration = 3000

root = tk.Tk()

screen_width = (root.winfo_screenwidth() if root.winfo_screenwidth() < 1920 else 1920)-10
screen_height = (root.winfo_screenheight() if root.winfo_screenheight() < 1080 else 1080 )-10

img = Image.open("logo.jpg")
img = img.resize((screen_width,screen_height))
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image = photo)
label.pack()

root.after(splash_screen_duration, label.destroy)

default_bind_address = tk.StringVar()
default_bind_port = tk.StringVar()

default_broadcast_addr = tk.StringVar()
default_broadcast_port = tk.StringVar()

#live_events = ScrollableTextFrame(tk.Frame(root,bg='black'))




def submit():

    global listen_addr
    global listen_port

    global bcast_addr
    global bcast_port

    listen_addr=default_bind_address.get()
    listen_port=int(default_bind_port.get())

    bcast_addr = default_broadcast_addr.get()
    bcast_port = int(default_broadcast_port.get())
    
    print("The list_addr is : ", listen_addr)
    print("The listen_port is : ", listen_port)

    print("The list_addr is : ", bcast_addr)
    print("The listen_port is : ", bcast_port)



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


red_box_label = tk.Label(red_base, text="ID                            Name                           Hardware ID", font=("Arial", 12), bg="red", fg="white")
red_box_label.grid(row=1, column=0, columnspan=10, pady=5)


green_box_label = tk.Label(green_base, text="ID                            Name                           Hardware ID", font=("Arial", 12), bg="green", fg="white")
green_box_label.grid(row=1, column=0, columnspan=10, pady=5)





def network_frame():
    global network_frame
    network_frame = tk.Frame(root,height=150,width=280,bg='black')
    network_frame.place(x=1550,y=250)

    global bind_addr
    global bind_port
    global bcast_addr
    global bcast_port
    

    widget_label = tk.Label(network_frame, text = 'Network Interface', font=('calibre',12, 'bold'),fg="red",bg="black")
    widget_label.grid(row=0,column=1,padx=2)

    bind_addr_label = tk.Label(network_frame, text = 'Bind Address: ', font=('calibre',10),fg="white",bg="black")
    bind_addr_label.grid(row=1,column=0,pady=2)
    bind_addr_entry = tk.Entry(network_frame, font=('calibre',10,'normal'),textvariable=default_bind_address)
    bind_addr_entry.insert(0,"0.0.0.0")
    bind_addr_entry.grid(row=1,column=1,pady=2)

    bind_addr = bind_addr_entry.get()

    bind_port_label = tk.Label(network_frame, text = 'Bind Port: ', font=('calibre',10),fg="white",bg="black")
    bind_port_label.grid(row=2,column=0,pady=2)
    bind_port_entry = tk.Entry(network_frame, font=('calibre',10,'normal'),textvariable=default_bind_port)
    bind_port_entry.insert(0,"7501")
    bind_port_entry.grid(row=2,column=1,pady=2)

    bind_port = bind_port_entry.get()

    transmit_addr_label = tk.Label(network_frame, text = 'Broadcast Address: ', font = ('calibre',10),fg="white",bg="black")
    transmit_addr_label.grid(row=3,column=0)
    transmit_addr_entry=tk.Entry(network_frame, font = ('calibre',10,'normal'),textvariable=default_broadcast_addr)
    transmit_addr_entry.grid(row=3,column=1,pady=2)
    transmit_addr_entry.insert(0,"127.0.0.1")

    bcast_addr = transmit_addr_entry.get()

    transmit_port_label = tk.Label(network_frame, text = 'Broadcast Port: ', font = ('calibre',10),fg="white",bg="black")
    transmit_port_label.grid(row=4,column=0)
    transmit_port_entry=tk.Entry(network_frame, font = ('calibre',10,'normal'),textvariable=default_broadcast_port)
    transmit_port_entry.grid(row=4,column=1,pady=2)
    transmit_port_entry.insert(0,"7500")

    bcast_port = transmit_port_entry.get()


def create_entry_grid(red_frame,green_frame):
    root.after(3000,network_frame)

    for row in range(2,22):  #20 rows
        red_details = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
        red_values[row-1] = red_details

        green_details = [tk.StringVar(),tk.StringVar(),tk.StringVar()]
        green_values[row-1] = green_details

        red_entry0 = tk.Entry(red_frame, width=5, textvariable=red_details[0])
        red_entry0.grid(row=row+1, column=0, padx=1, pady=3, sticky="ew")
        red_details[0].widget = red_entry0

        red_entry1 = tk.Entry(red_frame, width=25, textvariable=red_details[1])
        red_entry1.grid(row=row+1, column=1, padx=1, pady=3, sticky="ew")
        red_details[1].widget = red_entry1

        red_entry2 = tk.Entry(red_frame, width=25, textvariable=red_details[2])
        red_entry2.grid(row=row+1, column=2, padx=1, pady=3, sticky="ew")
        red_details[2].widget = red_entry2

        red_widget_dict[(row+1, 0)] = red_entry0
        red_widget_dict[(row+1, 1)] = red_entry1


        green_entry0 = tk.Entry(green_frame, width=5, textvariable=green_details[0])
        green_entry0.grid(row=row+1, column=0, padx=1, pady=3, sticky="ew")
        green_details[0].widget = green_entry0

        green_entry1 = tk.Entry(green_frame, width=25, textvariable=green_details[1])
        green_entry1.grid(row=row+1, column=1, padx=1, pady=3, sticky="ew")
        green_details[0].widget = green_entry1

        green_entry2 = tk.Entry(green_frame, width=25, textvariable=green_details[2])
        green_entry2.grid(row=row+1, column=2, padx=1, pady=3, sticky="ew")
        green_details[1].widget = green_entry2

        green_widget_dict[(row+1, 0)] = green_entry0
        green_widget_dict[(row+1, 1)] = green_entry1

        red_entry0.bind("<KeyRelease>", lambda event: update_player_name(event, red_details[0], red_details[1],red_widget_dict))

        green_entry0.bind("<KeyRelease>", lambda event: update_player_name(event, green_entry0, green_entry1,green_widget_dict))




create_entry_grid(red_base,green_base)

def update_player_name(event, entry_id, name_entry,widget_dict):
    active_widget = root.focus_get()
    player_id = active_widget.get()
    info = active_widget.grid_info()
    row, column = info["row"], info["column"]
    result=None
    print('calling',player_id)

    if player_id:
        try:
            photon_db.execute_query(f"SELECT codename FROM players WHERE id = {player_id}")
            result = photon_db.fetch_results()
        except:
            pass
    print(result)
    
    if result:
        next_widget = widget_dict.get((row, column + 1))
        next_widget.insert(1, result[0])


def check_for_duplicates_and_numbers():
    return True





def countdown_timer(root, reference_frame, pregame_duration=30, game_duration=360, start_callback=None, end_callback=None):   
    timer_label = tk.Label(reference_frame, text=f"{pregame_duration} sec", font=("Monotone", 80), fg="black", bg="white")
    timer_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def update_timer(time_left: int, is_pregame=True):
        if time_left > 0:
            timer_label.config(text=f"{time_left} sec")
            root.after(1000, lambda: update_timer(time_left - 1, is_pregame))
            if time_left == 17:
                photon_player.play_random_track()
        else:
            if is_pregame:
                # Pregame countdown finished → Start game countdown
                timer_label.config(text="Start!", fg="green")
                if start_callback:
                    start_callback()  # Execute game start action
                root.after(1000, lambda: update_timer(game_duration, is_pregame=False))
            else:
                # Game countdown finished
                timer_label.config(text="Game\nOver!", fg="red")
                if end_callback:
                    end_callback()  # Execute game end action

    update_timer(pregame_duration, is_pregame=True)



def editGame():
    pass
def gameParameters():
    unwrap_entries()

def tx_startcode():
    photon_server.broadcast_code("202")
    print("Start Code 202 Sent")

def tx_endcode():
    photon_player.stop_track()
    photon_server.broadcast_code("221")
    print("End Code 221 Sent")
    photon_server.broadcast_code("221")
    print("End Code 221 Sent")
    photon_server.broadcast_code("221")
    print("End Code 221 Sent")
    photon_server.stop()
    photon_db.conn.close()


def preEnteredGames():
    if check_for_duplicates_and_numbers():
        submit()
        network_frame.destroy()

        unwrap_entries()

        for i in red_values.keys():
            player_id = red_values[i][0]
            name = red_values[i][1]
            h_id = red_values[i][2]
            team = 'R'
            this_game.add_player(Player(player_id=player_id,player_name=name,hardware_id=h_id,team_name=team))

        for i in green_values.keys():
            player_id = green_values[i][0]
            name = green_values[i][1]
            h_id = green_values[i][2]
            team = 'G'
            this_game.add_player(Player(player_id=player_id,player_name=name,hardware_id=h_id,team_name=team))

        this_game.display_game_state()


        root_label.config(text="Live Events")
        if current_screen == "PlayerEntry":
            base.grid_forget()
            base.destroy()

            live_base = tk.Frame(root,height=400,width=1000,bg='white')
            live_base.pack()

            red_live = tk.Frame(live_base,height=400,width=500,bg='red',padx=30, pady=0)
            red_live.pack(side='left')

            global red_live_tree
            global green_live_tree
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
            
            global label_red_total

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

            global label_green_total

            label_green_total = tk.Label(green_live, text="Total Score: 0", font=("Arial", 14, "bold"), bg="green", fg="white")
            label_green_total.place(x=300,y=380)


            for i in red_values.keys():
                name = (red_values[i])[1]
                h_id = (red_values[i])[2]
                if len(name) > 0:
                    red_live_tree.insert("", 'end', text ="L1", values =(name, h_id, "0"))


            for i in green_values.keys():
                name = (green_values[i])[1]
                h_id = (green_values[i])[2]
                if len(name) > 0:
                    green_live_tree.insert("", 'end', text ="L1", values =(name, h_id, "0"))
            


            event_live_scroll = tk.Frame(root,height=400,width=1000,bg='white')
            event_live_scroll.pack()

            label_live = tk.Label(event_live_scroll, text="Live Events", font=("Arial", 12,), fg="black", bg="white")
            label_live.place(relx=0.5, rely=0.08, anchor="center")

            live_events = ScrollableTextFrame(event_live_scroll)

            global photon_server
            photon_server = Server(recv_addr=listen_addr,
                                    recv_port=listen_port,
                                    bcast_addr=bcast_addr,
                                    bcast_port=bcast_port,
                                    game_obj=this_game,
                                    scrollframe_obj=live_events
                                )
            photon_server.start()


            global timer_canvas
            timer_canvas = tk.Frame(root,height=350,width=350,bg='white')
            timer_canvas.place(x=1500,y=350)
    else:
        pass

def update_scores():
    for item in green_live_tree.get_children():
        row_data = green_live_tree.item(item)["values"]
        player = this_game.get_player_by_hardware_id(str(row_data[1]))
        new_score = player.score
        green_live_tree.item(item, values=(green_live_tree.item(item)['values'][0], 
                                        green_live_tree.item(item)['values'][1], 
                                        new_score))
    for item in red_live_tree.get_children():
        row_data = red_live_tree.item(item)["values"]
        player = this_game.get_player_by_hardware_id(str(row_data[1]))
        new_score = player.score
        red_live_tree.item(item, values=(red_live_tree.item(item)['values'][0], 
                                        red_live_tree.item(item)['values'][1], 
                                        new_score))

    
    label_green_total.config(text = f"Total Score: {this_game.total_team_score('G')}")

    label_red_total.config(text = f"Total Score: {this_game.total_team_score('R')}")

    if this_game.total_team_score('G') > this_game.total_team_score('R'):
        label_green_total.config(fg='yellow')
        label_red_total.config(fg="white")
    else:
        label_green_total.config(fg='white')
        label_red_total.config(fg="yellow")
    
    root.after(200, update_scores)


def init_hardware(event):
    active_widget = root.focus_get()
    info = active_widget.grid_info()
    row, column = info["row"], info["column"]
    temp_server = Server(recv_addr=bind_addr,
                                    recv_port=int(bind_port),
                                    bcast_addr=bcast_addr,
                                    bcast_port=int(bcast_port),
                                    scrollframe_obj=tk.Frame
                                )
    if column == 2:
        h_id = active_widget.get()
        temp_server.broadcast_code(active_widget.get())
        print('Init Hardware id:',h_id)
    del temp_server



def startGame():
    current_screen = "Live"
    update_scores()
    timer = countdown_timer(root,timer_canvas, pregame_duration=pregame_timer, game_duration=game_timer, 
                  start_callback=tx_startcode, end_callback=tx_endcode)


    

def viewGame():
    unwrap_entries()

    print(red_values)

    print("===")

    print(green_values)

def flickSync():
    print(photon_server.shooter_name)

def clearGame():
    if current_screen == "PlayerEntry":
        create_entry_grid(red_base)
        create_entry_grid(green_base)

red_players = {}

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
    
        for i in list(red_values.keys()):
            if len(red_values[i][0]) <= 0 and len(red_values[i][1]) <= 0:
                del red_values[i]

        for j in list(green_values.keys()):
            if len(green_values[j][0]) <= 0 and len(green_values[j][1]) <= 0:
                del green_values[j]



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
root.bind("<Tab>", init_hardware)



root.mainloop()
