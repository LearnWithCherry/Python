import tkinter as tk
from tkinter import messagebox
import random
import json
import os

# -------------------- FILE SETUP --------------------
HIGH_SCORE_FILE = "highscore.txt"
LEADERBOARD_FILE = "leaderboard.json"

# Load high score
if os.path.exists(HIGH_SCORE_FILE):
    with open(HIGH_SCORE_FILE, "r") as f:
        high_score = int(f.read())
else:
    high_score = 0

# Load leaderboard
if os.path.exists(LEADERBOARD_FILE):
    with open(LEADERBOARD_FILE, "r") as f:
        leaderboard = json.load(f)
else:
    leaderboard = {}

# -------------------- MAIN GAME LOGIC --------------------
class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Guess The Number")
        self.root.geometry("400x400")
        self.username = ""
        self.computer_number = None
        self.max_attempts = 5
        self.current_attempt = 0
        self.upper_limit = 10

        self.build_start_screen()

    def build_start_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter Your Name").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Choose Level").pack()
        self.level = tk.StringVar(value="easy")
        for val in ["easy", "mid", "hard"]:
            tk.Radiobutton(self.root, text=val.title(), variable=self.level, value=val).pack()

        tk.Label(self.root, text="Number of Attempts").pack()
        self.attempt_entry = tk.Entry(self.root)
        self.attempt_entry.insert(0, "5")
        self.attempt_entry.pack()

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

    def start_game(self):
        self.username = self.name_entry.get().strip()
        if not self.username:
            messagebox.showerror("Error", "Please enter a name.")
            return

        level = self.level.get()
        self.upper_limit = {"easy": 10, "mid": 25, "hard": 50}.get(level, 10)

        try:
            self.max_attempts = int(self.attempt_entry.get())
        except ValueError:
            messagebox.showwarning("Warning", "Invalid attempt number. Using default 5.")
            self.max_attempts = 5

        self.current_attempt = 1
        self.computer_number = random.randint(1, self.upper_limit)
        self.build_game_screen()

    def build_game_screen(self):
        self.clear_screen()
        tk.Label(self.root, text=f"Hello {self.username}!").pack()
        tk.Label(self.root, text=f"Guess a number between 1 and {self.upper_limit}").pack()
        tk.Label(self.root, text=f"Attempt {self.current_attempt}/{self.max_attempts}").pack()

        self.guess_entry = tk.Entry(self.root)
        self.guess_entry.pack()

        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack()

        tk.Button(self.root, text="Submit Guess", command=self.check_guess).pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="🚫 Enter a valid number!")
            return

        if guess < 1 or guess > self.upper_limit:
            self.feedback_label.config(text=f"⚠️ Between 1 and {self.upper_limit} only!")
            return

        diff = abs(guess - self.computer_number)

        if guess == self.computer_number:
            self.feedback_label.config(text="✅ Correct!")
            self.finish_game(win=True)
        else:
            if diff <= 2:
                self.feedback_label.config(text="🔥 You're very close!")
            elif guess < self.computer_number:
                self.feedback_label.config(text="⬆️ Too low!")
            else:
                self.feedback_label.config(text="⬇️ Too high!")

            self.current_attempt += 1
            if self.current_attempt > self.max_attempts:
                self.finish_game(win=False)
            else:
                self.build_game_screen()

    def finish_game(self, win):
        score = 100 - (self.current_attempt - 1) * 10 if win else 0
        msg = f"✅ You Won in {self.current_attempt - 1} attempts!\nScore: {score}" if win else f"💥 You lost! Number was {self.computer_number}\nScore: 0"

        global high_score
        if win and score > high_score:
            high_score = score
            with open(HIGH_SCORE_FILE, "w") as f:
                f.write(str(high_score))
            msg += "\n🔥 New High Score!"

        if win and (self.username not in leaderboard or score > leaderboard[self.username]):
            leaderboard[self.username] = score
            with open(LEADERBOARD_FILE, "w") as f:
                json.dump(leaderboard, f)

        messagebox.showinfo("Game Over", msg)
        self.show_leaderboard()

    def show_leaderboard(self):
        self.clear_screen()
        tk.Label(self.root, text="🏆 Leaderboard (Top Players)").pack()
        sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for name, scr in sorted_board[:5]:
            tk.Label(self.root, text=f"{name} : {scr}").pack()

        tk.Button(self.root, text="Play Again", command=self.build_start_screen).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# -------------------- RUN THE GAME --------------------
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessGame(root)
    root.mainloop()
