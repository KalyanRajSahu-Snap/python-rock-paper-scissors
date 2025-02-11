import tkinter as tk
from tkinter import ttk
import random
import os
from pygame import mixer
import base64
import tempfile

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x600")
        self.root.configure(bg='#FFCDB2')
        
        mixer.init()
        self.create_sound_files()
        
        self.player_score = 0
        self.computer_score = 0
        
        self.create_styles()
        
        self.main_frame = ttk.Frame(root, style='Main.TFrame', padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        title_label = ttk.Label(
            self.main_frame,
            text="ROCK PAPER SCISSORS",
            style='Title.TLabel'
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=20)
        
        self.create_score_display()
        self.create_choice_buttons()
        self.create_result_display()
        self.create_reset_button()
        
        self.win_streak = 0
        self.best_streak = 0
        self.streak_label = ttk.Label(
            self.main_frame,
            text="Current Streak: 0 | Best Streak: 0",
            style='Streak.TLabel'
        )
        self.streak_label.grid(row=6, column=0, columnspan=3, pady=10)

    def create_sound_files(self):
        self.temp_dir = tempfile.mkdtemp()
        self.button_sound_path = os.path.join(self.temp_dir, "button.wav")
        self.win_sound_path = os.path.join(self.temp_dir, "win.wav")
        self.lose_sound_path = os.path.join(self.temp_dir, "lose.wav")

    def create_styles(self):
        style = ttk.Style()
        
        style.configure('Main.TFrame', background='#FFCDB2')
        
        style.configure('Title.TLabel', 
                       font=('Helvetica', 24, 'bold'),
                       foreground='#B5828C',
                       background='#FFCDB2')
        
        style.configure('Game.TButton',
                       padding=15,
                       font=('Helvetica', 14, 'bold'))
        
        style.map('Game.TButton',
                 background=[('active', '#E5989B'), ('!active', '#FFB4A2')],
                 foreground=[('active', '#FFCDB2'), ('!active', '#B5828C')])
        
        style.configure('Score.TLabel',
                       font=('Helvetica', 18, 'bold'),
                       foreground='#E5989B',
                       background='#FFCDB2')
        
        style.configure('Result.TLabel',
                       font=('Helvetica', 14),
                       foreground='#B5828C',
                       background='#FFCDB2')
        
        style.configure('Streak.TLabel',
                       font=('Helvetica', 12),
                       foreground='#E5989B',
                       background='#FFCDB2')

    def create_score_display(self):
        self.score_frame = ttk.Frame(self.main_frame, style='Main.TFrame')
        self.score_frame.grid(row=1, column=0, columnspan=3, pady=20)
        
        self.player_score_label = ttk.Label(
            self.score_frame,
            text="Player: 0",
            style='Score.TLabel'
        )
        self.player_score_label.grid(row=0, column=0, padx=20)
        
        self.computer_score_label = ttk.Label(
            self.score_frame,
            text="Computer: 0",
            style='Score.TLabel'
        )
        self.computer_score_label.grid(row=0, column=1, padx=20)

    def create_choice_buttons(self):
        choices_frame = ttk.Frame(self.main_frame, style='Main.TFrame')
        choices_frame.grid(row=2, column=0, columnspan=3, pady=20)
        
        choices = ["🗿 Rock", "📄 Paper", "✂️ Scissors"]
        for i, choice in enumerate(choices):
            btn = ttk.Button(
                choices_frame,
                text=choice,
                style='Game.TButton',
                command=lambda c=choice: self.play_game(c.split()[1])
            )
            btn.grid(row=0, column=i, padx=10)

    def create_result_display(self):
        self.result_frame = ttk.Frame(self.main_frame, style='Main.TFrame')
        self.result_frame.grid(row=3, column=0, columnspan=3, pady=20)
        
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

    def create_reset_button(self):
        self.reset_button = ttk.Button(
            self.main_frame,
            text="🔄 Reset Game",
            style='Game.TButton',
            command=self.reset_game
        )
        self.reset_button.grid(row=5, column=0, columnspan=3, pady=20)

    def play_sound(self, sound_type):
        try:
            if sound_type == 'click':
                mixer.Sound(self.button_sound_path).play()
            elif sound_type == 'win':
                mixer.Sound(self.win_sound_path).play()
            elif sound_type == 'lose':
                mixer.Sound(self.lose_sound_path).play()
        except:
            pass

    def play_game(self, player_choice):
        self.play_sound('click')
        
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        choice_emojis = {
            "Rock": "🗿 Rock",
            "Paper": "📄 Paper",
            "Scissors": "✂️ Scissors"
        }
        
        self.player_choice_label.config(
            text=f"Your choice: {choice_emojis[player_choice]}"
        )
        self.computer_choice_label.config(
            text=f"Computer's choice: {choice_emojis[computer_choice]}"
        )
        
        if player_choice == computer_choice:
            result = "🤝 It's a tie!"
            self.win_streak = 0
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Paper" and computer_choice == "Rock") or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "🎉 You win!"
            self.player_score += 1
            self.win_streak += 1
            self.best_streak = max(self.win_streak, self.best_streak)
            self.play_sound('win')
        else:
            result = "😢 Computer wins!"
            self.computer_score += 1
            self.win_streak = 0
            self.play_sound('lose')
        
        self.result_label.config(text=result)
        self.update_score()
        self.update_streak()

    def update_score(self):
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")

    def update_streak(self):
        self.streak_label.config(
            text=f"Current Streak: {self.win_streak} | Best Streak: {self.best_streak}"
        )

    def reset_game(self):
        self.play_sound('click')
        self.player_score = 0
        self.computer_score = 0
        self.win_streak = 0
        self.best_streak = 0
        self.player_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer's choice: ")
        self.result_label.config(text="Make your choice!")
        self.update_score()
        self.update_streak()

def main():
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()