import tkinter as tk
from tkinter import ttk
from typing import Dict, List, Optional
import pygubu
from network import Network
from player import Player

def build_player_action_screen(root: tk.Tk, users: Dict[str, List[Player]], network: Network, main_frame: tk.Frame,
                               return_to_entry_screen, builder, entry_ids, db, user_data) -> None:
    # Load the player action UI and set up the action screen
    builder = pygubu.Builder()
    builder.add_from_file("assets/backgrounds/player_actions.ui")

    action_frame = builder.get_object("action_frame", root)
    action_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Configure the team tables
    blue_team_tree = create_team_treeview(action_frame, "Blue Team", 0.05)
    red_team_tree = create_team_treeview(action_frame, "Red Team", 0.55)

    # Create and place cumulative score labels
    blue_team_score_label = tk.Label(action_frame, text="Blue Team Score: 0", font=("Helvetica", 12))
    blue_team_score_label.place(relx=0.05, rely=0.35, anchor=tk.NW)

    red_team_score_label = tk.Label(action_frame, text="Red Team Score: 0", font=("Helvetica", 12))
    red_team_score_label.place(relx=0.55, rely=0.35, anchor=tk.NW)

    # Get the action_textbox from the builder and set it up
    #action_textbox: tk.Text = builder.get_object("action_textbox", action_frame)

    # Populate the teams
    populate_team_treeview(blue_team_tree, users.get("blue", []))
    populate_team_treeview(red_team_tree, users.get("red", []))

    # Create and place the leading team label
    leading_team_label = tk.Label(action_frame, text="Leading Team: None", font=("Helvetica", 14), fg="black")
    leading_team_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # Update the score labels initially
    update_team_scores(blue_team_score_label, red_team_score_label, users, leading_team_label)

    # Configure buttons
    play_button: tk.Button = builder.get_object("play_button", action_frame)
    play_button.configure(command=lambda: start_countdown(root, action_frame, users, network))

    back_button: tk.Button = builder.get_object("back_button", action_frame)
    back_button.configure(
        command=lambda: return_to_entry_screen(root, action_frame, main_frame, builder, entry_ids, users, db)
    )


def create_team_treeview(parent: tk.Frame, team_name: str, relx: float) -> ttk.Treeview:
    tree = ttk.Treeview(parent, columns=("Base", "ID", "Codename", "Score"), show="headings")
    for col in ("Base", "ID", "Codename", "Score"):
        tree.heading(col, text=col)
        tree.column(col, width=50 if col == "ID" else 100)
    tree.place(relx=relx, rely=0.1, anchor=tk.NW)

    # Styling
    style = ttk.Style()
    style.configure(f"{team_name}.Treeview", background="lightblue" if team_name == "Blue Team" else "lightcoral")
    tree.configure(style=f"{team_name}.Treeview")
    return tree


def populate_team_treeview(tree: ttk.Treeview, users: List[Player]) -> None:
    for user in users:
        tree.insert("", "end", values=(user.has_hit_base, user.user_id, user.codename, user.game_score))



def start_countdown(root: tk.Tk, action_frame: tk.Frame, users: Dict[str, List[Player]], network: Network,
                    count: int = 30, countdown_label: Optional[tk.Label] = None) -> None:
    if countdown_label is None:
        countdown_label = tk.Label(action_frame, text=str(count), font=("Helvetica", 64))
        countdown_label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    if count > 0:
        countdown_label.config(text=str(count))
        root.after(1000, start_countdown, root, action_frame, users, network, count - 1, countdown_label)
    else:
        countdown_label.destroy()


def update_team_scores(blue_team_score_label: tk.Label, red_team_score_label: tk.Label, users: Dict[str, List[Player]],
                       leading_team_label: tk.Label) -> None:
    # Calculate cumulative score for Blue Team
    blue_score = sum(user.game_score for user in users.get("blue", []))
    red_score = sum(user.game_score for user in users.get("red", []))

    # Update the score labels
    blue_team_score_label.config(text=f"Blue Team Score: {blue_score}")
    red_team_score_label.config(text=f"Red Team Score: {red_score}")

    # Update the leading team label
    if blue_score > red_score:
        leading_team_label.config(text=f"Leading Team: Blue Team ({blue_score} points)", fg="blue")
    elif red_score > blue_score:
        leading_team_label.config(text=f"Leading Team: Red Team ({red_score} points)", fg="red")
    else:
        leading_team_label.config(text="Leading Team: Tie", fg="black")