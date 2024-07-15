import tkinter as tk
from tkinter import messagebox
import random

# Function to start a new game
def new_game():
    global random_number
    random_number = random.randint(1, 100)
    guess_entry.delete(0, tk.END)
    feedback_label.config(text="Guess a number between 1 and 100")

# Function to check the user's guess
def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < random_number:
            feedback_label.config(text="Too low! Try again.")
        elif guess > random_number:
            feedback_label.config(text="Too high! Try again.")
        else:
            feedback_label.config(text="Congratulations! You guessed it!")
            messagebox.showinfo("Success", "You guessed the number!")
            new_game()
    except ValueError:
        feedback_label.config(text="Please enter a valid number")

# Set up the main application window
root = tk.Tk()
root.geometry("300x150")
root.title("Number Guessing Game")

# Set up the widgets
prompt_label = tk.Label(root, text="Enter your guess:")
prompt_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack()

feedback_label = tk.Label(root, text="Guess a number between 1 and 100")
feedback_label.pack()

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack()

# Start a new game
new_game()

# Run the application
root.mainloop()