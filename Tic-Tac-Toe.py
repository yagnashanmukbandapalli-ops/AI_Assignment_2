board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]

def display():
    for row in board:
        print(" | ".join(row))
        print("-"*5)

player = "X"

for i in range(9):
    display()
    
    r = int(input("Enter row (0-2): "))
    c = int(input("Enter column (0-2): "))
    
    if board[r][c] == " ":
        board[r][c] = player
    else:
        print("Already filled")
        continue
    
    # Check rows, columns, diagonals
    if (board[0][0]==board[0][1]==board[0][2]==player or
        board[1][0]==board[1][1]==board[1][2]==player or
        board[2][0]==board[2][1]==board[2][2]==player or
        board[0][0]==board[1][0]==board[2][0]==player or
        board[0][1]==board[1][1]==board[2][1]==player or
        board[0][2]==board[1][2]==board[2][2]==player or
        board[0][0]==board[1][1]==board[2][2]==player or
        board[0][2]==board[1][1]==board[2][0]==player):
        
        display()
        print(player,"wins")
        break
    
    player = "O" if player=="X" else "X"

display()
