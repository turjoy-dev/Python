import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Sudoku Solver")
        self.cells = {} # Dictionary to store entry widgets
        self.create_grid()
        
       
        solve_btn = tk.Button(root, text="Solve Board", command=self.run_solver, 
                              bg="#4CAF50", fg="white", font=('Arial', 12, 'bold'))
        solve_btn.grid(row=10, column=0, columnspan=9, pady=20)

    def create_grid(self):
        """Creates the 9x9 input grid"""
        for r in range(9):
            for c in range(9):
                # Add thicker borders for 3x3 subgrids
                p_x, p_y = (1, 1)
                if c % 3 == 0 and c != 0: p_x = (5, 1)
                if r % 3 == 0 and r != 0: p_y = (5, 1)
                
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center', borderwidth=2)
                entry.grid(row=r, column=c, padx=p_x, pady=p_y)
                self.cells[(r, c)] = entry

    def get_board(self):
        """Extracts values from the GUI into a 2D list"""
        board = []
        for r in range(9):
            row = []
            for c in range(9):
                val = self.cells[(r, c)].get()
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def update_grid(self, board):
        """Updates the GUI with the solved values"""
        for r in range(9):
            for c in range(9):
                self.cells[(r, c)].delete(0, tk.END)
                self.cells[(r, c)].insert(0, str(board[r][c]))
                self.cells[(r, c)].config(fg="blue")

    def is_valid(self, board, num, pos):
       
        for i in range(9):
            if board[pos[0]][i] == num and pos[1] != i: return False
            if board[i][pos[1]] == num and pos[0] != i: return False
        
        bx, by = pos[1] // 3, pos[0] // 3
        for i in range(by*3, by*3+3):
            for j in range(bx*3, bx*3+3):
                if board[i][j] == num and (i,j) != pos: return False
        return True

    def solve(self, board):
        """Standard Backtracking Solver"""
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, num, (r, c)):
                            board[r][c] = num
                            if self.solve(board):
                                return True
                            board[r][c] = 0
                    return False
        return True

    def run_solver(self):
        current_board = self.get_board()
        if self.solve(current_board):
            self.update_grid(current_board)
        else:
            messagebox.showerror("Error", "This puzzle has no solution!")

if __name__ == "__main__":
    root = tk.Tk()
    SudokuGUI(root)
    root.mainloop()