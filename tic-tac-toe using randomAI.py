import tkinter as tk
import random

# Set up the initial game board and score
board = [" " for _ in range(9)]
buttons = []
player_score = 0
ai_score = 0

# Function to check if a player has won
def check_win(mark):
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in combos:
        a, b, c = combo
        if board[a] == mark and board[b] == mark and board[c] == mark:
            return True
    return False

# Function to check for draw
def check_draw():
    for space in board:
        if space == " ":
            return False
    return True

# Disable all buttons once game is over
def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

# Called when player clicks a button
def player_click(index):
    global player_score
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")
        
        if check_win("X"):
            status_label.config(text="You win!")
            disable_buttons()
            player_score += 1
            update_score()
            return
        elif check_draw():
            status_label.config(text="Draw!")
            return

        ai_move()

# Random AI move
def ai_move():
    global ai_score
    empty_spots = []
    for i in range(len(board)):
        if board[i] == " ":
            empty_spots.append(i)
    
    if empty_spots:
        choice = random.choice(empty_spots)
        board[choice] = "O"
        buttons[choice].config(text="O", state="disabled")

        if check_win("O"):
            status_label.config(text="AI wins!")
            disable_buttons()
            ai_score += 1
            update_score()
        elif check_draw():
            status_label.config(text="Draw!")

# Update score display and who is leading
def update_score():
    score_label.config(text=f"You: {player_score}  |  AI: {ai_score}")
    if player_score > ai_score:
        lead_label.config(text="You're ahead!")
    elif ai_score > player_score:
        lead_label.config(text="AI is leading.")
    else:
        lead_label.config(text="Scores are tied.")

# Reset game board
def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")
    status_label.config(text="")
    lead_label.config(text="")

# Set up the UI
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create grid of buttons
for i in range(9):
    button = tk.Button(root, text=" ", width=6, height=3, font=("Arial", 20), command=lambda i=i: player_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Labels for status and scores
status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(root, text="You: 0  |  AI: 0", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3)

lead_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
lead_label.grid(row=5, column=0, columnspan=3)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
