from view import App
from view import pregame_screen


App = App()


App.resizable(False, False)
screen_width = (App.winfo_screenwidth() if App.winfo_screenwidth() < 1900 else 1900)-5
screen_height = (App.winfo_screenheight() if App.winfo_screenheight() < 1050 else 1050 )-10
App.geometry(f"{screen_width}x{screen_height}")


App.bind("<Escape>", lambda event: App.quit())
App.bind("<F5>", lambda event: App.goto_pregame_screen())
App.bind("<F12>", lambda event: App.frames['player_entry_screen'].clear_all_entries())
App.mainloop()
