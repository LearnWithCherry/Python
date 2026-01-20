import tkinter as tk
from tkinter import ttk, messagebox
import random, time, json, os
from datetime import datetime

# ---------------- CONFIG ----------------
HIGH_SCORE_FILE = "highscore.txt"
LEADERBOARD_FILE = "leaderboard.json"

# ---------------- DATA HANDLING ----------------
def load_high_score():
    return int(open(HIGH_SCORE_FILE).read()) if os.path.exists(HIGH_SCORE_FILE) else 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

def load_leaderboard():
    return json.load(open(LEADERBOARD_FILE)) if os.path.exists(LEADERBOARD_FILE) else []

def save_leaderboard(board):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(board, f, indent=2)

# ---------------- MAIN GAME CLASS ----------------
class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess The Number - Pro Edition")
        self.root.geometry("450x500")
        self.root.resizable(False, False)

        self.high_score = load_high_score()
        self.leaderboard = load_leaderboard()

        self.username = ""
        self.max_attempts = 5
        self.upper_limit = 10
        self.current_attempt = 0
        self.computer_number = None
        self.start_time = None

        self.show_start_screen()

    # ---------------- Start Menu ----------------
    def show_start_screen(self):
        self.clear_screen()

        ttk.Label(self.root, text="🎯 Guess The Number", font=("Arial", 20, "bold")).pack(pady=10)
        ttk.Label(self.root, text=f"🏆 High Score: {self.high_score}", font=("Arial", 12, "italic")).pack()

        ttk.Label(self.root, text="Enter Your Name:").pack()
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack()

        ttk.Label(self.root, text="Choose Difficulty:").pack(pady=5)
        self.level = tk.StringVar(value="easy")
        for val, num in [("Easy (1-10)", "easy"), ("Mid (1-25)", "mid"), ("Hard (1-50)", "hard")]:
            ttk.Radiobutton(self.root, text=val, variable=self.level, value=num).pack()

        ttk.Label(self.root, text="Number of Attempts:").pack(pady=5)
        self.attempt_entry = ttk.Entry(self.root)
        self.attempt_entry.insert(0, "5")
        self.attempt_entry.pack()

        ttk.Button(self.root, text="🚀 Start Game", command=self.start_game).pack(pady=15)
        ttk.Button(self.root, text="🏆 View Leaderboard", command=self.show_leaderboard).pack()

    # ---------------- Game Screen ----------------
    def start_game(self):
        self.username = self.name_entry.get().strip()
        if not self.username:
            messagebox.showerror("Error", "Please enter your name!")
            return
        
        difficulty = {"easy": 10, "mid": 25, "hard": 50}
        self.upper_limit = difficulty.get(self.level.get(), 10)

        try:
            self.max_attempts = int(self.attempt_entry.get())
        except ValueError:
            self.max_attempts = 5

        self.computer_number = random.randint(1, self.upper_limit)
        self.current_attempt = 1
        self.start_time = time.time()

        self.build_game_screen()

    def build_game_screen(self):
        self.clear_screen()

        ttk.Label(self.root, text=f"Hello {self.username}! 🎮", font=("Arial", 14, "bold")).pack(pady=5)
        ttk.Label(self.root, text=f"Guess a number between 1 and {self.upper_limit}").pack()
        self.attempt_label = ttk.Label(self.root, text=f"Attempt {self.current_attempt}/{self.max_attempts}")
        self.attempt_label.pack()

        self.guess_entry = ttk.Entry(self.root)
        self.guess_entry.pack(pady=5)
        self.guess_entry.focus()

        self.feedback_label = ttk.Label(self.root, text="", font=("Arial", 10, "italic"))
        self.feedback_label.pack()

        ttk.Button(self.root, text="Submit Guess", command=self.check_guess).pack(pady=10)

    # ---------------- Game Logic ----------------
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
            self.finish_game(True)
        else:
            if diff <= 2:
                self.feedback_label.config(text="🔥 Very close!")
            elif guess < self.computer_number:
                self.feedback_label.config(text="⬆️ Too low!")
            else:
                self.feedback_label.config(text="⬇️ Too high!")

            self.current_attempt += 1
            self.attempt_label.config(text=f"Attempt {self.current_attempt}/{self.max_attempts}")

            if self.current_attempt > self.max_attempts:
                self.finish_game(False)

    # ---------------- End Game ----------------
    def finish_game(self, win):
        time_taken = round(time.time() - self.start_time, 2)
        score = max(0, 100 - (self.current_attempt - 1) * 10 - int(time_taken))

        msg = f"✅ You won! Score: {score}\nNumber: {self.computer_number}\nTime: {time_taken}s" if win else f"💥 You lost! The number was {self.computer_number}."

        if win and score > self.high_score:
            self.high_score = score
            save_high_score(score)
            msg += "\n🔥 New High Score!"

        if win:
            self.leaderboard.append({"name": self.username, "score": score, "date": datetime.now().strftime("%d-%m-%Y %H:%M")})
            self.leaderboard = sorted(self.leaderboard, key=lambda x: x['score'], reverse=True)[:10]
            save_leaderboard(self.leaderboard)

        messagebox.showinfo("Game Over", msg)
        self.show_leaderboard()

    # ---------------- Leaderboard ----------------
    def show_leaderboard(self):
        self.clear_screen()
        ttk.Label(self.root, text="🏆 Leaderboard", font=("Arial", 16, "bold")).pack(pady=5)
        for i, player in enumerate(self.leaderboard, start=1):
            ttk.Label(self.root, text=f"{i}. {player['name']} - {player['score']} ({player['date']})").pack()

        ttk.Button(self.root, text="Play Again", command=self.show_start_screen).pack(pady=5)
        ttk.Button(self.root, text="Exit Game", command=self.root.quit).pack()

    # ---------------- Helpers ----------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ---------------- RUN GAME ----------------
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    game = GuessGame(root)
    root.mainloop()
