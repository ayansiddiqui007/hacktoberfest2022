import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.board = [""] * 9
        
        self.buttons = []
        for i in range(9):
            row, col = i // 3, i % 3
            button = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=row, column=col)
            self.buttons.append(button)
        
    def make_move(self, position):
        if self.board[position] == "" and not self.check_winner():
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.current_player == "X":
                self.current_player = "O"
                self.make_ai_move()
            else:
                self.current_player = "X"
            winner = self.check_winner()
            if winner:
                if winner == "tie":
                    self.show_message("It's a tie!")
                else:
                    self.show_message(f"Player {winner} wins!")
                self.disable_buttons()
        
    def make_ai_move(self):
        # Simple AI: Randomly choose an empty spot
        empty_spots = [i for i in range(9) if self.board[i] == ""]
        if empty_spots:
            ai_move = random.choice(empty_spots)
            self.make_move(ai_move)
        
    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and self.board[combo[0]] != "":
                return self.board[combo[0]]
        if "" not in self.board:
            return "tie"
        return None
    
    def show_message(self, message):
        popup = tk.Toplevel()
        popup.title("Game Over")
        label = tk.Label(popup, text=message, font=("Helvetica", 16))
        label.pack(padx=20, pady=20)
        restart_button = tk.Button(popup, text="Restart", font=("Helvetica", 12), command=self.restart)
        restart_button.pack(pady=10)
        
    def restart(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.enable_buttons()
        
    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
            
    def enable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
