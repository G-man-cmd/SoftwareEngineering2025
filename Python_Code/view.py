import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from PIL import Image, ImageTk
from tkinter import ttk
from tkscrolledframe import ScrolledFrame
from scrollframe import ScrollableTextFrame
from tkscrolledframe import ScrolledFrame
from tkinter import messagebox

from current_game import CurrentGame,Player
from music import RandomTrackPlayer
from database import Database
from server import Server



class player_entry_screen(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg='black')
        self.controller = controller

        self.frame_title = tk.Label(self, bg='black', fg='white', text="Player Entry Screen", font=("Arial", 20, "bold"))
        self.frame_title.pack(pady=10)

        self.default_bind_address = tk.StringVar()
        self.default_bind_port = tk.StringVar()
        self.default_broadcast_addr = tk.StringVar()
        self.default_broadcast_port = tk.StringVar()

        self.red_values = {}
        self.green_values = {}

        self.red_widget_dict = {}
        self.green_widget_dict = {}

        self.name_focus_empty_flags = {}

        self.root = tk.Frame(self, bg="white", height=1000, width=1920)
        self.root.pack(pady=20)

        self.base = tk.Frame(self.root, height=700, width=1000, bg='white')
        self.base.pack()

        self.red_base = tk.Frame(self.base, height=700, width=500, bg='red', padx=30, pady=0)
        self.red_base.pack(side='left')
        self.red_base.grid_propagate(0)
        self.label_red = tk.Label(self.red_base, text="RED TEAM", font=("Arial", 14, "bold"), bg="red", fg="white")
        self.label_red.grid(row=0, column=0, columnspan=10, pady=5)

        self.green_base = tk.Frame(self.base, height=700, width=500, bg='green', padx=30, pady=0)
        self.green_base.pack(side='right')
        self.green_base.grid_propagate(0)
        self.label_green = tk.Label(self.green_base, text="GREEN TEAM", font=("Arial", 14, "bold"), bg="green", fg="white")
        self.label_green.grid(row=0, column=0, columnspan=10, pady=5)

        self.red_box_label = tk.Label(self.red_base, text="ID                            Name                           Hardware ID", font=("Arial", 12), bg="red", fg="white")
        self.red_box_label.grid(row=1, column=0, columnspan=10, pady=5)

        self.green_box_label = tk.Label(self.green_base, text="ID                            Name                           Hardware ID", font=("Arial", 12), bg="green", fg="white")
        self.green_box_label.grid(row=1, column=0, columnspan=10, pady=5)

        for row in range(2, 22):  # 20 rows
            red_details = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
            self.red_values[row - 1] = red_details

            green_details = [tk.StringVar(), tk.StringVar(), tk.StringVar()]
            self.green_values[row - 1] = green_details

            red_entry0 = tk.Entry(self.red_base, width=5, textvariable=red_details[0])
            red_entry0.bind("<Tab>", lambda event, details=red_details: self.fill_player_name(event, details))
            red_entry0.grid(row=row + 1, column=0, padx=1, pady=3, sticky="ew")
            red_details[0].widget = red_entry0

            red_entry1 = tk.Entry(self.red_base, width=25, textvariable=red_details[1])
            red_entry1.bind("<FocusIn>", lambda event, row=row, team="red": self.check_if_empty(event, row, team))
            red_entry1.bind("<FocusOut>", lambda event, row=row, details=red_details, team="red": self.insert_unknown(event, row, team, details))
            red_entry1.grid(row=row + 1, column=1, padx=1, pady=3, sticky="ew")
            red_details[1].widget = red_entry1

            red_entry2 = tk.Entry(self.red_base, width=25, textvariable=red_details[2])
            red_entry2.bind("<Tab>", lambda event, var=red_details[2]: self.init_hardware(event, var))
            red_entry2.grid(row=row + 1, column=2, padx=1, pady=3, sticky="ew")
            red_details[2].widget = red_entry2

            self.red_widget_dict[(row + 1, 0)] = red_entry0
            self.red_widget_dict[(row + 1, 1)] = red_entry1

            green_entry0 = tk.Entry(self.green_base, width=5, textvariable=green_details[0])
            green_entry0.bind("<Tab>", lambda event, details=green_details: self.fill_player_name(event, details))
            green_entry0.grid(row=row + 1, column=0, padx=1, pady=3, sticky="ew")
            green_details[0].widget = green_entry0

            green_entry1 = tk.Entry(self.green_base, width=25, textvariable=green_details[1])
            green_entry1.bind("<FocusIn>", lambda event, row=row, team="green": self.check_if_empty(event, row, team))
            green_entry1.bind("<FocusOut>", lambda event, row=row, details=green_details, team="green": self.insert_unknown(event, row, team, details))
            green_entry1.grid(row=row + 1, column=1, padx=1, pady=3, sticky="ew")
            green_details[1].widget = green_entry1

            green_entry2 = tk.Entry(self.green_base, width=25, textvariable=green_details[2])
            green_entry2.bind("<Tab>", lambda event, var=green_details[2]: self.init_hardware(event, var))
            green_entry2.grid(row=row + 1, column=2, padx=1, pady=3, sticky="ew")
            green_details[2].widget = green_entry2

            self.green_widget_dict[(row + 1, 0)] = green_entry0
            self.green_widget_dict[(row + 1, 1)] = green_entry1

    def clear_all_entries(self):
        for red_vars in self.red_values.values():
            for var in red_vars:
                var.set("")

        for green_vars in self.green_values.values():
            for var in green_vars:
                var.set("")


    def get_row_data_dicts(self):
        red_data = {}
        green_data = {}

        for row_index in range(2, 22):
            red_vars = self.red_values[f"{row_index - 1}"]
            green_vars = self.green_values[row_index - 1]

            red_row_values = tuple(var for var in red_vars)
            green_row_values = tuple(var for var in green_vars)

            red_data[row_index - 1] = red_row_values
            green_data[row_index - 1] = green_row_values

            self.red_values = red_data
            self.green_values = green_data
    
    def check_if_empty(self, event, row, team):
        widget = event.widget
        is_empty = widget.get().strip() == ""
        self.name_focus_empty_flags[(row, team)] = is_empty

    def insert_unknown(self, event, row, team, details):
        was_empty = self.name_focus_empty_flags.get((row, team), False)
        new_name = details[1].get().strip()
        new_id = details[0].get().strip()
        if '(' in new_name:
            pass
        else:
            self.controller.photon_db.execute_query(f"INSERT INTO players (id,codename) values({new_id},'{new_name}');")
            print("New Player Inserted")

    def extract_values(self, data):
        cleaned_data = {}
        for key, (x, y, z) in data.items():
            x_val = x.get().strip()
            y_val = y.get().strip()
            z_val = z.get().strip()
            if x_val and y_val and z_val:
                # Clean up y_val like "((\'Opus\',),)" to "Opus"
                y_clean = y_val.replace("(", "").replace(")", "").replace(",", "").replace("'", "").strip()
                cleaned_data[key] = (x_val, y_clean, z_val)
        return cleaned_data

    def make_player_dicts(self):
        self.controller.red_players = self.extract_values(self.red_values)
        self.controller.green_players = self.extract_values(self.green_values)

    def fill_player_name(self, event, details):
        widget = event.widget
        if widget.focus_get() == widget:
            player_id = details[0].get()
            player_name = details[1].get()
            try:
                self.controller.photon_db.execute_query(f"SELECT codename FROM players WHERE id = {player_id};")
                result = self.controller.photon_db.fetch_results()
                if len((result[0])[0]) > 0:
                    details[1].set(result)
            except:
                pass

        self.controller.bind("<Tab>", lambda event: self.init_hardware)

    def init_hardware(self, event, var):
        widget = event.widget
        if widget.focus_get() == widget:
            self.controller.photon_server.broadcast_code(var.get())

    def init_player(self):
        
        self.make_player_dicts()

        for i in self.controller.red_players.keys():
            player_id = self.controller.red_players[i][0]
            name = self.controller.red_players[i][1]
            h_id = self.controller.red_players[i][2]
            team = 'R'
            self.controller.this_game.add_player(Player(player_id=player_id,player_name=name,hardware_id=h_id,team_name=team))
            self.controller.frames['pregame_screen'].red_live_tree.insert("", 'end', text ="L1", values =(name, h_id, "0"))
    
        for i in self.controller.green_players.keys():
            player_id = self.controller.green_players[i][0]
            name = self.controller.green_players[i][1]
            h_id = self.controller.green_players[i][2]
            team = 'G'
            self.controller.this_game.add_player(Player(player_id=player_id,player_name=name,hardware_id=h_id,team_name=team))
            self.controller.frames['pregame_screen'].green_live_tree.insert("", 'end', text ="L1", values =(name, h_id, "0"))



class pregame_screen(tk.Frame):

    def start_countdown(self, pregame, game):
        if pregame == 17:
            self.controller.photon_player.play_random_track()

        if pregame > 0:
            self.timer_label.config(text=f"{pregame}")
            self.root.after(1000, self.start_countdown, pregame - 1, game)
        elif pregame == 0 and game > 0:
            self.controller.photon_server.broadcast_code("202")
            self.timer_label.config(text="Start")
            self.root.after(1000, self.start_game_countdown, game)
        else:
            self.controller.photon_server.broadcast_code("221")
            self.timer_label.config(text="Game\nOver")

    def start_game_countdown(self, game):
        if game > 0:
            self.timer_label.config(text=f"{game}")
            self.root.after(1000, self.start_game_countdown, game - 1)
        else:
            self.controller.photon_server.broadcast_code("221")
            self.controller.photon_player.stop_track()
            self.timer_label.config(text="Game\nOver")

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        self.root = tk.Frame(self, bg="black", height=1000, width=1920)
        self.root.pack(pady=10)
    
        self.frame_title = tk.Label(self.root,bg='black',fg='white',text="Live Play Screen",font=("Arial", 20, "bold"))
        self.frame_title.pack(pady=10)

        self.live_base = tk.Frame(self.root,height=400,width=1000,bg='white')
        self.live_base.pack()

        self.red_live = tk.Frame(self.live_base,height=400,width=500,bg='red',padx=30, pady=0)
        self.red_live.pack(side='left')

        global red_live_tree
        global green_live_tree
        self.red_live_tree = ttk.Treeview(self.red_live, selectmode ='browse',height=15)
        self.red_live_tree.pack(side ='right',anchor='s',pady=50)

        self.red_live_tree["columns"] = ("1", "2", "3")
        self.red_live_tree["show"] = 'headings'

        self.red_live_tree.column("1", width = 165, anchor ='c')
        self.red_live_tree.column("2", width = 90, anchor ='se')
        self.red_live_tree.column("3", width = 165, anchor ='se')

        self.verscrlbar = ttk.Scrollbar(self.red_live, 
                        orient ="vertical", 
                        command = self.red_live_tree.yview)
        self.verscrlbar.pack(side ='right', fill ='x')
        self.red_live_tree.configure(xscrollcommand = self.verscrlbar.set)

        self.red_live_tree.heading("1", text ="Name")
        self.red_live_tree.heading("2", text ="H_ID")
        self.red_live_tree.heading("3", text ="Score")

        self.label_red = tk.Label(self.red_live, text="RED TEAM", font=("Arial", 14, "bold"), bg="red", fg="white")
        self.label_red.place(relx=0.5, rely=0.05, anchor="center")
        
        global label_red_total

        self.label_red_total = tk.Label(self.red_live, text="Total Score: 0", font=("Arial", 14, "bold"), bg="red", fg="white")
        self.label_red_total.place(x=300,y=380)


        self.green_live = tk.Frame(self.live_base,height=400,width=500,bg='green',padx=30, pady=0)
        self.green_live.pack(side='right')
        self.green_live.grid_propagate(0)
        
        self.green_live_tree = ttk.Treeview(self.green_live, selectmode ='browse',height=15)
        self.green_live_tree.pack(side ='right',anchor='s',pady=50)

        self.green_live_tree["columns"] = ("1", "2", "3")
        self.green_live_tree["show"] = 'headings'

        self.green_live_tree.column("1", width = 165, anchor ='c')
        self.green_live_tree.column("2", width = 90, anchor ='se')
        self.green_live_tree.column("3", width = 165, anchor ='se')

        self.verscrlbar = ttk.Scrollbar(self.green_live, 
                        orient ="vertical", 
                        command = self.green_live_tree.yview)
        self.verscrlbar.pack(side ='right', fill ='x')
        self.red_live_tree.configure(xscrollcommand = self.verscrlbar.set)

        self.green_live_tree.heading("1", text ="Name")
        self.green_live_tree.heading("2", text ="H_ID")
        self.green_live_tree.heading("3", text ="Score")

        self.label_green = tk.Label(self.green_live, text="GREEN TEAM", font=("Arial", 14, "bold"), bg="green", fg="white")
        self.label_green.place(relx=0.5, rely=0.05, anchor="center")

        global label_green_total

        self.label_green_total = tk.Label(self.green_live, text="Total Score: 0", font=("Arial", 14, "bold"), bg="green", fg="white")
        self.label_green_total.place(x=300,y=380)

        self.event_live_scroll = tk.Frame(self.root,height=400,width=1000,bg='white')
        self.event_live_scroll.pack()

        self.label_live = tk.Label(self.event_live_scroll, text="Live Events", font=("Arial", 12,), fg="black", bg="white")
        self.label_live.place(relx=0.5, rely=0.08, anchor="center")

        self.live_events = ScrollableTextFrame(self.event_live_scroll)

        self.timer_label = tk.Label(self,text='Pregame\nTimer',font=('Helvitica',"40",'bold'),bg='black',fg='white')
        self.timer_label.place(x=1620,y=400)


class App(tk.Tk):

    def reset(self):
        print('reset')
        green_live_tree = self.frames['pregame_screen'].green_live_tree
        live_events = self.frames['pregame_screen'].live_events
        red_live_tree = self.frames['pregame_screen'].red_live_tree

        for i in green_live_tree.get_children():
            green_live_tree.delete(i)

        for i in red_live_tree.get_children():
            red_live_tree.delete(i)

        self.frames['pregame_screen'].label_green_total.config(text = "Total Score:0")
        self.frames['pregame_screen'].label_red_total.config(text = "Total Score:0")
        self.frames['pregame_screen'].label_green_total.config(fg = 'white')
        self.frames['pregame_screen'].label_red_total.config(fg = 'white')    
        
        live_events.clear_all_text()

        self.this_game.reset_game()

        self.frames['pregame_screen'].timer_label.config(text="Pregame\nTimer")

        self.show_frame("player_entry_screen")




    def __init__(self, *args, **kwargs):

        self.current_screen = 'player_entry_screen'

        self.bind_addr = "0.0.0.0"
        self.bind_port = 7501
        self.bcast_addr = "127.0.0.1"
        self.bcast_port = 7500

        self.red_players = {}
        self.green_players = {}

        self.photon_db = Database(dbname='photon')

        self.this_game = CurrentGame()

        self.photon_server = Server(recv_addr=self.bind_addr,
                        recv_port=int(self.bind_port),
                        bcast_addr=self.bcast_addr,
                        bcast_port=int(self.bcast_port),
                        controller = self
                    )

        self.track_list=["Track01.mp3","Track03.mp3","Track05.mp3" ,"Track07.mp3","Track02.mp3","Track04.mp3","Track06.mp3","Track08.mp3"]
        self.photon_player = RandomTrackPlayer(self.track_list)

        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self,width=1920,height=1080)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        def show_splash_screen(self):
            width = (self.winfo_screenwidth() if self.winfo_screenwidth() < 1900 else 1900)-5
            height = (self.winfo_screenheight() if self.winfo_screenheight() < 1050 else 1050 )-10

            self.splash_photo = Image.open("logo.jpg")

            self.splash_photo = self.splash_photo.resize((width,height))

            self.splash_photo = ImageTk.PhotoImage(self.splash_photo)

            self.splash_frame = tk.Frame(self, bg="black")
            self.splash_label = tk.Label(self.splash_frame, image=self.splash_photo, bg="black")
            self.splash_label.pack(expand=True, fill="both")
            self.splash_frame.place(x=0,y=0)

            self.splash_frame.after(3000,lambda : self.splash_frame.destroy())
        
        def remove_splash_screen(self):
            self.splash_frame.destroy()

        
        show_splash_screen(self)
        

        self.frames = {}

        for F in (player_entry_screen,pregame_screen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("player_entry_screen")


        buttonFrame = tk.Frame(self,bg="black")
        f1 = tk.Button(buttonFrame, text = "F1\n Edit \n Game", bg = "black", fg = "green", command=lambda: self.reset())
        f1.grid(row=0,column=1)
        f3 = tk.Button(buttonFrame, text = "F3\nPregame\nTimer", bg = "black", fg = "green", command= lambda: self.frames['pregame_screen'].start_countdown(20,10))
        f3.grid(row=0,column=2)
        f5 = tk.Button(buttonFrame, text = "F5\nPregame\n Screen", bg = "black", fg = "green", command=(lambda: self.goto_pregame_screen()))
        f5.grid(row=0,column=3)
        f12 = tk.Button(buttonFrame, text = "F12\nClear \nGame", bg = "black", fg = "green", command=(lambda: self.frames['player_entry_screen'].clear_all_entries()))
        f12.grid(row=0,column=6)

        self.after(3000,lambda : buttonFrame.place(x=800,y=800))

    
    def goto_pregame_screen(self):
        self.frames['player_entry_screen'].init_player()
        self.show_frame("pregame_screen")
        self.photon_server.start()


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        self.current_screen = page_name
        frame = self.frames[page_name]
        frame.tkraise()