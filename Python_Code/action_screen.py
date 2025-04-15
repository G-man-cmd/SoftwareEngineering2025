import tkinter as tk
from tkinter import ttk
from typing import Dict, List
from player_data import Player

#test player class to make sure it works properly. comment out before submit
class Player:
    def __init__(self, base:str, ID: str, Nickname: str, score: int):
        self.base = base
        self.ID = ID
        self.Nickname = Nickname
        self.score = score
    def player_reached_base(self, player: Player, team_table: ttk.Treeview) -> None:
        #update score?
        player.mark_reach_base()
        self.update_player_name(team_table, player.ID, player.Nickname)

class game_screen:
    def __init__(self, players: Dict[str, List[Player]]):
        self.players = players
        self.green_team_score = 0
        self.red_team_score = 0
        
    def create_game_action_screen(self, root: tk.Tk, screen: tk.Frame, return_to_player_entry, entry_ids, db, user_data) -> None:
        action_screen = tk.Frame(root, bg = "black")
        action_screen.place(x = 0, y = 0, width = 1600, height = 1000)
        red_team = self.put_team_on_screen(action_screen, "Red Team")
        green_team = self.put_team_on_screen(action_screen, "Green Team")
        red_total_score = tk.Label(action_screen, text = "Red's Score: 0", font = ("Monospace", 12))
        green_total_score = tk.Label(action_screen, text = "Green's Score: 0", font = ("Monospace", 12))
        red_total_score.place(relx = 0.05, rely = 0.35, anchor = tk.NW)
        green_total_score.place(relx = 0.55, rely = 0.35, anchor = tk.NW)

        self.enter_players(red_team, self.players.get("red", []))
        self.enter_players(green_team, self.players.get("green", []))
        # more functionality eventually

        countdown_button = tk.Button(action_screen, text = "Start Counter", command = lambda: self.timer(root, action_screen))
        countdown_button.place(relx = 0.5, rely = 0.7)
        
    def put_team_on_screen(self, reference_frame: tk.Frame, name: str) -> ttk.Treeview:
        xpos = None
        if name == "Green Team":
            xpos = 200
        else:
            xpos = 1000
        team_table = ttk.Treeview(reference_frame, columns = ("base", "ID", "Nickname", "Score"), show = "headings")
        for col in ("base", "ID", "Nickname", "Score"):
            team_table.heading(col, text = col)
            team_table.column(col, width = 50 if col == "ID" else 100)
        team_table.place(x = xpos, y = 100)
        return team_table
        
    def enter_players(self, team_table: ttk.Treeview, players: List[Player]) -> None:
        for player in players:
            team_table.insert("", "end", values=(player.base, player.ID, player.Nickname, player.score))
        
    #will need to be able to change scores
    def timer(self, root: tk.Tk, reference_frame: tk.Frame) -> None:
        self.time_left = 30
        self.timer_label = tk.Label(reference_frame, text = f"{self.time_left} sec", font = ("Monotone", 50), fg = "white", bg = "black")
        self.timer_label.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        self.update_timer(root)

    def update_timer(self, root: tk.Tk) -> None:
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text = f"{self.time_left} sec")
            root.after(1000, lambda: self.update_timer(root))
        else:
            self.timer_label.config(text = "Finished", fg = "red")

    def update_player_name(self, team_table: ttk.Treeview, player_id: str, new_name: str) -> None:
        for item in team_table.get_children():
            values = team_table.item(item, "values")
            if values[1] == player_id:
                team_table.item(item, values=(values[0], values[1], new_name, values[3]))
                break
    #will probably need to go back to player entry eventually
#delete or comment out everything below after testing it.