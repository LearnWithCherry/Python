import tkinter as tk
import random
import json
import os

BALANCE_FILE = "slot_balance.json"

# Load or initialize coin balance
def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            return json.load(f).get("coins", 100)
    return 100

# Save current coin balance
def save_balance(coins):
    with open(BALANCE_FILE, "w") as f:
        json.dump({"coins": coins}, f)

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Slot Machine")
        self.root.geometry("400x350")
        self.symbols = ["🍒", "🍋", "🔔", "💎", "🍊", "🍇"]
        self.coins = load_balance()

        self.build_ui()
        self.update_balance()

    def build_ui(self):
        # Slot display
        self.reel_frame = tk.Frame(self.root)
        self.reel_frame.pack(pady=30)

        self.reels = [tk.Label(self.reel_frame, text="❓", font=("Arial", 40)) for _ in range(3)]
        for r in self.reels:
            r.pack(side="left", padx=10)

        # Spin button
        self.spin_btn = tk.Button(self.root, text="🎲 SPIN (10 coins)", font=("Arial", 14), command=self.spin)
        self.spin_btn.pack(pady=10)

        # Message display
        self.message = tk.Label(self.root, text="", font=("Arial", 12))
        self.message.pack()

        # Balance
        self.balance_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.balance_label.pack()

        # Play again
        self.play_again_btn = tk.Button(self.root, text="Play Again", command=self.reset_game, state="disabled")
        self.play_again_btn.pack(pady=5)

    def update_balance(self):
        self.balance_label.config(text=f"💰 Coins: {self.coins}")
        save_balance(self.coins)

    def spin(self):
        if self.coins < 10:
            self.message.config(text="❌ Not enough coins!")
            self.spin_btn.config(state="disabled")
            self.play_again_btn.config(state="normal")
            return

        self.coins -= 10
        reels_result = [random.choice(self.symbols) for _ in range(3)]

        # Animate the spin
        for i in range(3):
            self.reels[i].config(text=reels_result[i])

        if reels_result[0] == reels_result[1] == reels_result[2]:
            self.coins += 50
            self.message.config(text="🎉 JACKPOT! You win 50 coins!")
        elif reels_result[0] == reels_result[1] or reels_result[1] == reels_result[2] or reels_result[0] == reels_result[2]:
            self.coins += 20
            self.message.config(text="👏 Two matched! You win 20 coins.")
        else:
            self.message.config(text="😢 No match. Try again!")

        self.update_balance()

        if self.coins < 10:
            self.message.config(text=self.message.cget("text") + " | No more spins left.")
            self.spin_btn.config(state="disabled")
            self.play_again_btn.config(state="normal")

    def reset_game(self):
        self.coins = 100
        save_balance(self.coins)
        self.update_balance()
        self.message.config(text="")
        for reel in self.reels:
            reel.config(text="❓")
        self.spin_btn.config(state="normal")
        self.play_again_btn.config(state="disabled")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachine(root)
    root.mainloop()
