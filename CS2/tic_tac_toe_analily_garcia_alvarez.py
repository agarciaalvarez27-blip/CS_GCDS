#Plan work work plan

def display_board(board):
    
    return board

def get_player_move(board):
    userxrow = input("Row you are positioning your X: ")
    userxcol = input("Column you are positioning your X: ")
    userorow = input("Row you are positioning your O: ")
    userocol = input("Column you are positioning your O: ")
    board[userxrow][userxcol]= "X"
    board[userorow][userocol]= "O"

def check_winner(board, player):
    winner = ""
    if board[0][0] == player and board [0][1] == player and board [0][2] == player:
        return True
    elif board[1][0] == player and board [1][1] == player and board [1][2] == player:
        return True
    elif board[2][0] == player and board [2][1] == player and board [2][2] == player:
        return True
    elif board[0][0] == player and board [1][0] == player and board [2][0] == player:
        return True
    elif board[0][1] == player and board [1][1] == player and board [2][1] == player:
        return True
    elif board[0][2] == player and board [1][2] == player and board [2][2] == player:
        return True
    elif board[0][0] == player and board [1][1] == player and board [2][2] == player:
        return True
    elif board[0][2] == player and board [1][1] == player and board [2][0] == player:
        return True
    else:
        return False

    return winner

#def is_draw(board):
 #   if board



def main():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    result = check_winner(board, "X")
    print(result)
    #while True


#   q 
#        break

    print(display_board(board))
    print(f"   1   2   3\n1  {board[0][0]} | {board[0][1]} | {board[0][2]}\n  -----------\n2  {board[1][0]} | {board[1][1]} | {board[1][2]}\n  -----------\n3  {board[2][0]} | {board[2][1]} | {board[2][2]}")
    get_player_move(board)
    
main()