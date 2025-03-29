import tkinter as tk
from tkinter import ttk

screen = tk.Tk()
box = tk.Canvas(screen, width=200, height=500)
box2 = tk.Canvas(screen, width=200, height=500)
screen.title("Entry Terminal")
screen.geometry("1200x1200")
screen.configure(background="black")
tk.Label(screen, text="Edit Current Game", bg="black", height=4, width=40, bd=4, font=("Arial", 16, "bold"), fg="blue").pack()
box.create_rectangle(0,0,200,500, outline="red", fill="red")
box.place(relx=0.5, rely=0.5, anchor=tk.E)
frame1 = tk.Frame(box, width=400, height=800)
frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

box2.create_rectangle(0,0,200,500, outline="green", fill="green")
box2.pack()
box2.place(relx=0.5, rely=0.5, anchor=tk.W)
frame2 = tk.Frame(box2, width=400, height=800)
frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

table1 = ttk.Treeview(frame1) # keep table 1 inside the red box
table1['columns'] = ('num', 'RED TEAM')
table1.column('#0', width = 5, stretch = tk.NO)
table1.column('num', anchor=tk.W, width = 20)
table1.column('RED TEAM', anchor=tk.W, width = 150)
table1.heading('#0', text='RED TEAM', anchor=tk.W)
table1.heading('num', text='', anchor=tk.W)
table1.heading('RED TEAM', text='RED TEAM', anchor=tk.W)
table1.rowconfigure(19, {'minsize': 60})
table1.grid(column = 2, row = 19)
table1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


table2 = ttk.Treeview(frame2) #keep table 2 inside the green box
table2['columns'] = ('num', 'GREEN TEAM')
table2.column('#0', width = 5, stretch = tk.NO)
table2.column('num', anchor=tk.W, width = 20)
table2.column('GREEN TEAM', anchor=tk.W, width = 150)
table2.heading('#0', text='GREEN TEAM', anchor=tk.W)
table2.heading('num', text='', anchor=tk.W)
table2.heading('GREEN TEAM', text='GREEN TEAM', anchor=tk.W)
table2.grid(column = 2, row = 19)
table2.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

def editGame():
    pass
def gameParameters():
    pass
def startGame():
    pass
def preEnteredGames():
    pass
def viewGame():
    pass
def flickSync():
    pass
def clearGame():
    pass

buttonFrame = tk.Frame(screen, bg="black")
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

screen.bind("<F1>", lambda event: editGame())
screen.bind("<F2>", lambda event: gameParameters())
screen.bind("<F3>", lambda event: startGame())
screen.bind("<F5>", lambda event: preEnteredGames())
screen.bind("<F8>", lambda event: viewGame())
screen.bind("<F10>", lambda event: flickSync())
screen.bind("<F12>", lambda event: clearGame())

def new_row(table, item):
    all_items = table.get_children()
    if item == all_items[-1]:  # If editing the last row
        table.insert("", "end", values=("", ""))  # Add new empty row

def edit_cell(event, table):
    selected_item = table.selection()
    if not selected_item:
        return

    item = selected_item[0]
    column_id = table.identify_column(event.x)
    column_index = int(column_id.strip("#")) - 1  # Convert column ID to index
    
    if column_index < 0:
        return

    # Get current value
    x, y, width, height = table.bbox(item, column_id)
    entry = tk.Entry(table)
    entry.place(x=x, y=y, width=width, height=height)
    entry.insert(0, table.item(item, "values")[column_index])
    entry.focus()
    
    def save_edit(event):
        new_value = entry.get()
        values = list(table.item(item, "values"))
        values[column_index] = new_value
        table.item(item, values=(values,))
        entry.destroy()
        new_row(table, item)

    entry.bind("<Return>", save_edit)
    entry.bind("<FocusOut>", save_edit)
    entry.bind("<Tab>", lambda e: save_edit(e) or focus_next_entry(table, item, column_index))

def focus_next_entry(table, item, column_index):
    next_index = (column_index + 1) % len(table["columns"])
    table.selection_set(item)
    table.focus(item)
    table.update()
    table.event_generate("<Double-1>")
table1.bind("<Double-1>", lambda event: edit_cell(event, table1))
table2.bind("<Double-1>", lambda event: edit_cell(event, table2))  

table1.insert('', 'end', values=("", ""))
table2.insert('', 'end', values=("", ""))



screen.mainloop()
