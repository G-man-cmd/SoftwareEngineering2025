from typing import Dict, List
import os
import tkinter as tk
import psycopg2
from psycopg2 import sql

from network import Network
from db import Database  # Import the Database class
from player import Player
import splash_screen
import player_entry_page
import player_actions

if os.name == "nt":
    import winsound

# Define PostgreSQL connection parameters
connection_params = {
    'dbname': 'photon',
    'user': 'student',
    'password': 'student',
    'host': 'localhost',
    'port': '5432'
}

# Initialize the Database instance
db = Database()
db.connect()  # Establish the connection
db.create_table()


def build_root() -> tk.Tk:
    # Build main window, set title, make fullscreen
    root: tk.Tk = tk.Tk()
    root.title("Photon")
    root.configure(background="white")

    # Force window to fill screen, place at top left
    # width: int = root.winfo_screenwidth()
    # height: int = root.winfo_screenheight()
    # root.geometry(f"{width}x{height}+0+0")
    root.attributes('-fullscreen', True)
    # Disable resizing
    root.resizable(False, False)
    return root


def destroy_root(root: tk.Tk, network: Network) -> None:
    if os.name == "nt":
        winsound.PlaySound(None, winsound.SND_ASYNC)
    network.close_sockets()
    db.close()  # Close the database connection
    root.destroy()


# def show_player_action_screen(root: tk.Tk, users: Dict[str, List[Player]]) -> None:
#     """Displays the player action screen after player entry is completed."""
#     player_actions.PlayerAction(root, users)


def main() -> None:
    # Declare dictionary for storing user information
    # Format: { team: [User, User, ...] }
    users: Dict[str, List[Player]] = {
        "blue": [],
        "red": []
    }

    # Create networking object
    network: Network = Network()
    network.set_sockets()

    # Call build_root function to build the root window
    root: tk.Tk = build_root()

    # Bind escape key and window close button to destroy_root function
    root.bind("<Escape>", lambda event: destroy_root(root, network))
    root.protocol("WM_DELETE_WINDOW", lambda: destroy_root(root, network))

    # Build the splash screen
    splash: splash_screen = splash_screen.build(root)

    # After 3 seconds, destroy the splash screen and build the player entry screen
    # Pass the 'db' object along with other arguments
    root.after(3000, splash.destroy)
    root.after(3000, player_entry_page.build, root, users, network, db)  # Pass db to build function

    # Run the main loop
    root.mainloop()


if __name__ == "__main__":
    main()