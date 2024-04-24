import random
import tkinter as tk

class Team:
    def __init__(self, name):
        self.name = name
        self.goals_scored = 0

    def get_name(self):
        return self.name

    def get_goals_scored(self):
        return self.goals_scored

    def score_goal(self):
        self.goals_scored += 1

def simulate_match(team_a, team_b, output_text):
    match_duration = 90

    for minute in range(1, match_duration + 1):
        if random.random() < 0.05:
            if random.choice([True, False]):
                team_a.score_goal()
                output_text.insert(tk.END, f"\n{'-' * 80}\n                         GOAL FOR {team_a.get_name()} IN THE {minute}TH MINUTE!\n{'-' * 80}\n")
            else:
                team_b.score_goal()
                output_text.insert(tk.END, f"\n{'-' * 80}\n                         GOAL FOR {team_b.get_name()} IN THE {minute}TH MINUTE!\n{'-' * 80}\n")
            output_text.update_idletasks()

def simulate_quick_match_gui():
    def start_simulation():
        output_text.delete('1.0', tk.END)
        team1 = entry_team1.get()
        team2 = entry_team2.get()
        team_a = Team(team1)
        team_b = Team(team2)
        simulate_match(team_a, team_b, output_text)
        final_score = f"\n{'-' * 80}\n                         FINAL SCORE: {team_a.get_name()} {team_a.get_goals_scored()} - {team_b.get_goals_scored()} {team_b.get_name()}\n{'-' * 80}\n{'X' * 80}\n"
        output_text.insert(tk.END, final_score)
        back_button.pack(side=tk.BOTTOM)

    def back_to_menu():
        output_text.delete('1.0', tk.END)
        entry_team1.delete(0, tk.END)
        entry_team2.delete(0, tk.END)
        back_button.pack_forget()
        render_main_menu()

    root = tk.Tk()
    root.title("Quick Match Simulator")

    label_team1 = tk.Label(root, text="Enter the first team:")
    label_team1.pack()
    entry_team1 = tk.Entry(root)
    entry_team1.pack()

    label_team2 = tk.Label(root, text="Enter the second team:")
    label_team2.pack()
    entry_team2 = tk.Entry(root)
    entry_team2.pack()

    button_simulate = tk.Button(root, text="Simulate Match", command=start_simulation)
    button_simulate.pack()

    output_text = tk.Text(root, height=20, width=100)
    output_text.pack()

    back_button = tk.Button(root, text="Back to Main Menu", command=back_to_menu)

    root.mainloop()

def simulate_champions_league_gui():
    def start_simulation():
        output_text.delete('1.0', tk.END)
        teams = [entry_teams[i].get() for i in range(16)]
        simulate_champions_league(teams, output_text)
        back_button.pack(side=tk.BOTTOM)

    def back_to_menu():
        output_text.delete('1.0', tk.END)
        for entry in entry_teams:
            entry.delete(0, tk.END)
        back_button.pack_forget()
        render_main_menu()

    root = tk.Tk()
    root.title("Champions League Simulator")

    label_teams = tk.Label(root, text="Enter the 16 teams:")
    label_teams.pack()

    entry_teams = []
    for i in range(16):
        entry_team = tk.Entry(root)
        entry_team.pack()
        entry_teams.append(entry_team)

    button_simulate = tk.Button(root, text="Simulate Champions League", command=start_simulation)
    button_simulate.pack()

    output_text = tk.Text(root, height=20, width=100)
    output_text.pack()

    back_button = tk.Button(root, text="Back to Main Menu", command=back_to_menu)

    root.mainloop()

def simulate_champions_league(teams, output_text):
    ro16 = teams[:]
    ro8 = []
    sfnl = []
    fnl = []

    output_text.insert(tk.END, "-----------------------------------------ROUND OF 16------------------------------------------------\n")

    for i in range(1, 9):  # round of 16
        c = random.randint(0, 4)
        v = random.randint(0, 4)
        while c == v:
            c = random.randint(0, 4)
            v = random.randint(0, 4)
        s1 = ro16.pop(0)
        s2 = ro16.pop(0)
        output_text.insert(tk.END, f"                                    {s1} = {c}     vs     {s2} = {v}\n")
        if c > v:
            ro8.append(s1)
        else:
            ro8.append(s2)

    output_text.insert(tk.END, "\n---------------------------------------QUARTER FINALS----------------------------------------------\n")

    for j in range(1, 5):  # round of 8 (quarter finals)
        p = random.randint(0, 4)
        l = random.randint(0, 4)
        while p == l:
            p = random.randint(0, 4)
            l = random.randint(0, 4)
        s3 = ro8.pop(0)
        s4 = ro8.pop(0)
        output_text.insert(tk.END, f"                                    {s3} = {p}     vs     {s4} = {l}\n")
        if p > l:
            sfnl.append(s3)
        else:
            sfnl.append(s4)

    output_text.insert(tk.END, "\n-----------------------------------------SEMI FINALS------------------------------------------------\n")

    for k in range(1, 3):  # round of 4 (semi-finals)
        q = random.randint(0, 4)
        z = random.randint(0, 4)
        while q == z:
            q = random.randint(0, 4)
            z = random.randint(0, 4)
        s5 = sfnl.pop(0)
        s6 = sfnl.pop(0)
        output_text.insert(tk.END, f"                                    {s5} = {q}     vs     {s6} = {z}\n")
        if q > z:
            fnl.append(s5)
        else:
            fnl.append(s6)

    output_text.insert(tk.END, "\n--------------------------------------------FINALS--------------------------------------------------\n")

    f = random.randint(0, 4)
    m = random.randint(0, 4)
    while f == m:
        f = random.randint(0, 4)
        m = random.randint(0, 4)
    s7 = fnl.pop(0)
    s8 = fnl.pop(0)
    output_text.insert(tk.END, f"                                    {s7} = {f}     vs     {s8} = {m}\n")
    if f > m:
        output_text.insert(tk.END, "\n----------------------------------UEFA CHAMPIONS LEAGUE WINNER--------------------------------------\n")
        output_text.insert(tk.END, f"                                               {s7}\n")
        output_text.insert(tk.END, "----------------------------------------------------------------------------------------------------\n")
    else:
        output_text.insert(tk.END, "\n----------------------------------UEFA CHAMPIONS LEAGUE WINNER--------------------------------------\n")
        output_text.insert(tk.END, f"                                               {s8}\n")
        output_text.insert(tk.END, "----------------------------------------------------------------------------------------------------\n")

def render_main_menu():
    def handle_choice(choice):
        if choice == 1:
            root.destroy()
            simulate_quick_match_gui()
        elif choice == 2:
            root.destroy()
            simulate_champions_league_gui()
        elif choice == 3:
            root.destroy()
        else:
            print("Enter a valid choice")

    root = tk.Tk()
    root.title("Main Menu")

    label_options = tk.Label(root, text="Choose an option:")
    label_options.pack()

    button_quick_match = tk.Button(root, text="1. Simulate a Quick Match", command=lambda: handle_choice(1))
    button_quick_match.pack()

    button_champions_league = tk.Button(root, text="2. Simulate Champions League", command=lambda: handle_choice(2))
    button_champions_league.pack()

    button_exit = tk.Button(root, text="3. Exit", command=lambda: handle_choice(3))
    button_exit.pack()

    root.mainloop()

render_main_menu()
