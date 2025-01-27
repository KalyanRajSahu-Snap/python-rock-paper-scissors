import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x500")
        
        # Score tracking
        self.player_score = 0
        self.computer_score = 0
        
        # Style configuration
        style = ttk.Style()
        style.configure('Game.TButton', padding=10, font=('Helvetica', 12))
        style.configure('Score.TLabel', font=('Helvetica', 14))
        style.configure('Result.TLabel', font=('Helvetica', 12))
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Score display
        self.score_label = ttk.Label(
            self.main_frame,
            text="Score - Player: 0  Computer: 0",
            style='Score.TLabel'
        )
        self.score_label.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Player choice buttons
        self.create_choice_button("Rock", 1)
        self.create_choice_button("Paper", 2)
        self.create_choice_button("Scissors", 3)
        
        # Result display
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.grid(row=4, column=0, columnspan=3, pady=20)
        
        self.player_choice_label = ttk.Label(
            self.result_frame,
            text="Your choice: ",
            style='Result.TLabel'
        )
        self.player_choice_label.grid(row=0, column=0, pady=5)
        
        self.computer_choice_label = ttk.Label(
            self.result_frame,
            text="Computer's choice: ",
            style='Result.TLabel'
        )
        self.computer_choice_label.grid(row=1, column=0, pady=5)
        
        self.result_label = ttk.Label(
            self.result_frame,
            text="Make your choice!",
            style='Result.TLabel'
        )
        self.result_label.grid(row=2, column=0, pady=10)
        
        # Reset button
        self.reset_button = ttk.Button(
            self.main_frame,
            text="Reset Game",
            style='Game.TButton',
            command=self.reset_game
        )
        self.reset_button.grid(row=5, column=0, columnspan=3, pady=20)

    def create_choice_button(self, choice, column):
        button = ttk.Button(
            self.main_frame,
            text=choice,
            style='Game.TButton',
            command=lambda: self.play_game(choice)
        )
        button.grid(row=2, column=column-1, padx=10, pady=10)

    def play_game(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        self.player_choice_label.config(text=f"Your choice: {player_choice}")
        self.computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Paper" and computer_choice == "Rock") or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        
        self.result_label.config(text=result)
        self.update_score()

    def update_score(self):
        self.score_label.config(
            text=f"Score - Player: {self.player_score}  Computer: {self.computer_score}"
        )

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer's choice: ")
        self.result_label.config(text="Make your choice!")
        self.update_score()

def main():
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()