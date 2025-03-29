import tkinter as tk
from tkinter import ttk
from typing import Dict, List, Optional
#from network import Network #this is what is used to do networking stuff
from Python_Code.player_data import Player

def build_screen(root: tk.Tk, players: Dict[str, List[Player]], network: Network, main_frame: tk.Frame, return_to_entry, entry_ids, db, user_data)->None:
    #creates player entry screen
    action_frame = tk.Frame(root, bg = "white")
    action_frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER, relwidth = 0.9, relheight = 0.9)
    
    #team tables made here
    green_team = create_team(action_frame, "Green Team", 0.05)
    red_team = create_team(action_frame, "Red Team", 0.05)
    
    #total scores
    #green
    green_team_score = tk.Label(action_frame, text = "Green Team Score: 0", font = ("Helvetica", 12))
    green_team_score.place(relx = 0.05, rely = 0.35, anchor = tk.NW)
    #red
    red_team_score = tk.Label(action_frame, text = "Red Team Score: 0", font = ("Helvetica", 12))
    red_team_score.place(relx = 0.05, rely = 0.35, anchor = tk.NW)

    #fill teams
    populate_team(green_team, players.get("green", []))
    populate_team(red_team, players.get("red", []))

    #leading team label
    leading_team = tk.Label(action_frame, text = "Leading Team: None", font = ("Helvetica", 14), fg = "black")
    leading_team.place(relx = 0.5, rely = 0.05, anchor = tk.CENTER)

    #update scores here
    update_scores(green_team_score, red_team_score, players, leading_team)

    #makes buttons
    play_button = tk.Button(action_frame, text = "Start Countdown", command = lambda: timer(root, action_frame, players, network))
    play_button.place(relx = 0.5, rely = 0.7, anchor = tk.CENTER)

    return_button = tk.Button(action_frame, text = "Back", command = lambda: revert(root, action_frame, main_frame, entry_ids, players, db))
    return_button.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)

def create_team(parent: tk.Frame, team_name: str, relx: float) -> ttk.Treeview:
    #makes table for players on a team
    table = ttk.Treeview(parent, columns = ("Base", "ID", "Nickname", "Score"), show = "headings")
    for col in ("Base", "ID", "Nickname", "Score"):
        table.heading(col, text = col)
        table.column(col, width = 50 if col == "ID" else 100)

    table.place(relx = relx, rely = 0.1, anchor = tk.NW)

    theme = ttk.Style()
    theme.configure(f"{team_name}.Treeview", background = "lightgreen" if team_name == "Green Team" else "lightcoral")
    table.configure(theme = f"{team_name}.Treeview")

    return table

def populate_team(table: ttk.Treeview, players: List[Player]) -> None:
    for player in players:
        table.insert("", "end", values = (player.base, player.ID, player.Nickname, player.score))

def timer(root: tk.Tk, action_frame: tk.Frame, players: Dict[str, List[Player]], network: Network, count: int = 30, counter: Optional[tk.Label] = None) -> None:
    if counter is None:
        counter = tk.Label(action_frame, text = str(count), font = ("Helvetica", 64))
        counter.place(relx = 0.5, rely = 0.55, anchor = tk.CENTER)
    if count > 0:
        counter.config(text = str(count))
        root.after(1000, timer, root, action_frame, players, network, count - 1, counter)
    else:
        counter.destroy()
    
def revert(root: tk.Tk, action_frame: tk.Frame, main_frame: tk.Frame, ids, players, db):
    action_frame.destroy()
    main_frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

def update_scores(green_score: tk.Label, red_score: tk.Label, players: Dict[str, List[Player]], lead: tk.Label) -> None:
    green = sum(player.score for player in players.get("green", []))
    red = sum(player.score for player in players.get("red", []))

    green_score.config(text = f"Green team Score: {green}")
    red_score.config(text = f"Red team Score: {red}")

    if green > red:
        lead.config(text = f"Leading Team: Green Team ({green} points)", fg = "green")
    elif red > green:
        lead.config(text = f"Leading Team: Red Team ({red} points)", fg = "red")
    else:
        lead.config(text = "Leading team: Tie", fg = "black")