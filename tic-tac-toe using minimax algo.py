# # Simple Tic-Tac-Toe with AI using Tkinter

import tkinter as tk

# Game Setup

board = [" " for _ in range(9)]
your_score = 0
ai_score = 0

# Game Logic

def check_winner(b, mark):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(b[i] == mark for i in combo) for combo in winning_combinations)

def is_draw(b):
    return all(cell != " " for cell in b)

# Minimax Algorithm

def minimax(b, depth, is_ai):
    if check_winner(b, "O"):
        return 10 - depth
    if check_winner(b, "X"):
        return depth - 10
    if is_draw(b):
        return 0

    if is_ai:
        max_eval = -float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                eval = minimax(b, depth + 1, False)
                b[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                eval = minimax(b, depth + 1, True)
                b[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

def find_best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# UI Functions

def handle_click(idx):
    global your_score, ai_score

    if board[idx] != " " or check_winner(board, "X") or check_winner(board, "O"):
        return
    

    # Your move
    board[idx] = "X"
    buttons[idx].config(text="X", state="disabled")

    if check_winner(board, "X"):
        your_score += 1
        update_status("You win!")
        update_scoreboard()
        disable_all_buttons()
        return

    if is_draw(board):
        update_status("It's a Draw.")
        return
    
    # AI move
    ai_move = find_best_move()
    if ai_move != -1:
        board[ai_move] = "O"
        buttons[ai_move].config(text="O", state="disabled")

    if check_winner(board, "O"):
        ai_score += 1
        update_status("AI wins.")
        update_scoreboard()
        disable_all_buttons()
    elif is_draw(board):
        update_status("It's a Draw.")
    
# Score Updates
def update_scoreboard():
    player_label.config(text=f"Your Score: {your_score}")
    ai_label.config(text=f"AI Score: {ai_score}")

def update_status(msg):
    status_label.config(text=msg)

def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")


# Reset the Game
def reset_board():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")
    update_status("")

# Tkinter UI
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text=" ", font=("Calibri", 22), width=7, height=3,
                    command=lambda i=i: handle_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Scoreboard and Controls
player_label = tk.Label(root, text="Your Score: 0", font=("Calibri", 13))
player_label.grid(row=3, column=0)

ai_label = tk.Label(root, text="AI Score: 0", font=("Calibri", 13))
ai_label.grid(row=3, column=1)

reset_button = tk.Button(root, text="Reset", font=("Calibri", 14), command=reset_board)
reset_button.grid(row=3, column=2)

status_label = tk.Label(root, text="", font=("Times New Roman", 14), fg="blue")
status_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
