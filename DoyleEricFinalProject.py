import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Change the background color of the main window
window.configure(bg="#021347")

# Create four labels
label1 = tk.Label(text="Toronto Maple Leafs", bg="#021347", fg="white")
label1.pack()

label2 = tk.Label(text="Schedule Tracker", bg="#021347", fg="white")
label2.pack()

label4 = tk.Label(text="&", bg="#021347", fg="white")
label4.pack()

label3 = tk.Label(text="Points Tracker", bg="#021347", fg="white")
label3.pack()

# Create three buttons
def home_games_clicked():
    # Create the pop-up window
    pop_up_window = tk.Toplevel()
    pop_up_window.title("Home Games Pop-Up")

    # Create a list in the pop-up window
    list_frame = tk.Frame(pop_up_window)
    list_frame.pack(side="left", fill="both", expand=True)

    listbox = tk.Listbox(list_frame)
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(list_frame, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    for item in ["vs Ottawa Senators 4-1 W", "vs Ottawa Senators 4-2 L", "vs Montreal Canadiens 3-0 W",
                 "vs Detroit Red Wings 4-2 L", "vs Washington Capitals 3-2 W", "vs Ottawa Senators 3-2 W",
                 "vs Arizona Coyotes 4-2 L", "vs Dallas Stars 3-2 W", "vs Philadelphia Flyers 5-2 W",
                 "vs Boston Bruins 2-1 W", "vs Vegas Golden Knights 4-3 L", "vs Pittsburgh Penguins 5-2 W",
                 "vs New Jersey Devils 3-2 L", "vs Buffalo Sabres 5-2 W", "vs New York Islanders 3-2 L",
                 "vs San Jose Sharks 3-1 W", "vs LA Kings 5-0 W", "vs Calgary Flames 5-4 W",
                 "vs Anaheim Ducks 7-0 W", ]:
        listbox.insert("end", item)

    # Create a space for an image in the pop-up window
    image_frame = tk.Frame(pop_up_window)
    image_frame.pack(side="right", fill="both", expand=True)

    image_label = tk.Label(image_frame)
    image_label.pack(fill="both", expand=True)

    # Create an "Exit" button to close the pop-up window
    def exit_clicked():
        pop_up_window.destroy()

    exit_button = tk.Button(pop_up_window, text="Exit", bg="#021347", fg="black", command=exit_clicked)
    exit_button.pack()

home_games_button = tk.Button(text="Home Games", bg="#021347", fg="black", command=home_games_clicked)
home_games_button.pack()

def away_games_clicked():
    # Create the pop-up window
    pop_up_window = tk.Toplevel()
    pop_up_window.title("Away Games Pop-Up")

    # Create a list in the pop-up window
    list_frame = tk.Frame(pop_up_window)
    list_frame.pack(side="left", fill="both", expand=True)

    listbox = tk.Listbox(list_frame)
    listbox.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(list_frame, orient="vertical")
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")

    listbox.config(yscrollcommand=scrollbar.set)

    for item in ["@ Ottawa Senators 6-3 W", "@ Montreal Canadiens 5-1 W", "@ Detroit Red Wings 4-2 L",
                 "@ Montreal Canadiens 4-3 L", "@ Winnipeg Jets 4-1 W", "@ Vegas Golden Knights 3-1 L",
                 "@ San Jose Sharks 4-3 L", "@ LA Knights 4-2 L", "@ Anaheim Ducks 4-3 L",
                 "@ Carolina Hurricanes 3-1 W", "@ Pittsburgh Penguins 5-2 W", "@ New Jersey Devils 2-1 W",
                 "@ Minnesota Wild 4-3 W", "@ Pittsburgh Penguins 4-1 W", "@ Detroit Red Wings 4-2 W",
                 "@ Tampa Bay Lightning 4-3 L", "@ Dallas Stars 4-0 W", "@ New York Rangers 3-1 L",
                 "@ Washington Capitals 3-1 L"]:
        listbox.insert("end", item)

    # Create a space for an image in the pop-up window
    image_frame = tk.Frame(pop_up_window)
    image_frame.pack(side="right", fill="both", expand=True)

    image_label = tk.Label(image_frame)
    image_label.pack(fill="both", expand=True)

    # Create an "Exit" button to close the pop-up window
    def exit_clicked():
        pop_up_window.destroy()

    exit_button = tk.Button(pop_up_window, text="Exit", bg="#021347", fg="black", command=exit_clicked)
    exit_button.pack()

away_games_button = tk.Button(text="Away Games", bg="#021347", fg="black", command=away_games_clicked)
away_games_button.pack()

def points_clicked():
    # Create the pop-up window
    pop_up_window = tk.Toplevel()
    pop_up_window.title("Point Leaders")

    # Create three columns of text in the pop-up window
    column1_frame = tk.Frame(pop_up_window)
    column1_frame.pack(side="left", fill="both", expand=True)

    column1_label = tk.Label(column1_frame, text="Goals\nWilliam Nylander - 18\nAuston Matthews - 16\nJohn Tavares - 14")
    column1_label.pack(fill="both", expand=True)

    column2_frame = tk.Frame(pop_up_window)
    column2_frame.pack(side="left", fill="both", expand=True)

    column2_label = tk.Label(column2_frame, text="Assists\nMitch Marner - 25\nAuston Matthews - 21\nWilliam Nylander - 16\nJohn Tavares - 16")
    column2_label.pack(fill="both", expand=True)

    column3_frame = tk.Frame(pop_up_window)
    column3_frame.pack(side="left", fill="both", expand=True)

    column3_label = tk.Label(column3_frame, text="Points\nAuston Matthews - 37\nMitch Marner - 37\nWilliam Nylander - 34\nJohn Tavares - 30")
    column3_label.pack(fill="both", expand=True)

    # Create an "Exit" button to close the pop-up window
    def exit_clicked():
        pop_up_window.destroy()

    exit_button = tk.Button(pop_up_window, text="Exit", bg="#021347", fg="black", command=exit_clicked)
    exit_button.pack()

points_button = tk.Button(text="Point Leaders", bg="#021347", fg="black", command=points_clicked)
points_button.pack()


# Create a button to exit the program
def exit_clicked():
    window.destroy()

exit_button = tk.Button(text="Exit", bg="#021347", fg="black", command=exit_clicked)
exit_button.pack()

# Run the main loop
window.mainloop()
