"""
Name: Mohammad Fakhro
Class: CSCI 1411-004
Due Date: 11/3/2026
Description: Tic-Tac-Toe Game with 2D Lists
Status: Works 
"""

def reset_grid(grid):
    for i in range(3):
        for j in range(3):
            grid[i][j] = ' '

def check_row(grid, row_num):
    if grid[row_num][0] == grid[row_num][1] == grid[row_num][2] and grid[row_num][0] != ' ':
        return True
    return False

def check_column(grid, col_num):
    if grid[0][col_num] == grid[1][col_num] == grid[2][col_num] and grid[0][col_num] != ' ':
        return True
    return False

def check_diagonal(grid, diagonal):
    if diagonal == "d1":
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
            return True
    elif diagonal == "d2":
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
            return True
    return False

def place_entry(grid, row_num, col_num, ch):
    if grid[row_num][col_num] == ' ':
        grid[row_num][col_num] = ch
        return True
    return False

def playable(grid):
    for row in grid:
        for cell in row:
            if cell == ' ':
                return True
    return False

def print_grid(grid):
    print("-----------------")
    for row in grid:
        row_str = ""
        for cell in row:
            row_str += f"| {cell} "
        row_str += "|"
        print(row_str)
        print("-----------------")

def main():
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    player1_n = input("Player 1 enter your name: ")
    player2_n = input("Player 2 enter your name: ")
    
    current_player = player1_n
    current_ch = 'x'

    while True:
        rowcol = input(f"{current_player} Enter location to be marked (row, col): ")
        
        try:
            row_str, col_str = rowcol.strip().replace(',', ' ').split()
            row = int(row_str)
            col = int(col_str)
        except ValueError:
            print("Error: Invalid format. Please enter two numbers separated by a space.")
            continue

        if row not in [1, 2, 3] or col not in [1, 2, 3]:
            print("Error: Your row or column number is out of bound")
            if current_player == player1_n:
                current_player, current_ch = player2_n, 'o'
            else:
                current_player, current_ch = player1_n, 'x'
            continue

        r_idx = row - 1
        c_idx = col - 1

        if not place_entry(grid, r_idx, c_idx, current_ch):
            print("That location is already taken")
            if current_player == player1_n:
                current_player, current_ch = player2_n, 'o'
            else:
                current_player, current_ch = player1_n, 'x'
            continue

        print_grid(grid)

        won = False
        if check_row(grid, r_idx):
            won = True
        elif check_column(grid, c_idx):
            won = True
        elif (r_idx == c_idx and check_diagonal(grid, "d1")) or (r_idx + c_idx == 2 and check_diagonal(grid, "d2")):
            won = True

        if won:
            print(f"{current_player} You won the game")
            play_again = input("Do you want to play again (y or n)? ")
            if play_again.lower().startswith('y'):
                reset_grid(grid)
                current_player = player1_n
                current_ch = 'x'
                continue
            else:
                break

        if not playable(grid):
            print("The game is a draw!")
            play_again = input("Do you want to play again (y or n)? ")
            if play_again.lower().startswith('y'):
                reset_grid(grid)
                current_player = player1_n
                current_ch = 'x'
                continue
            else:
                break

        # Switch turns smoothly if game continues
        if current_player == player1_n:
            current_player, current_ch = player2_n, 'o'
        else:
            current_player, current_ch = player1_n, 'x'

main()
