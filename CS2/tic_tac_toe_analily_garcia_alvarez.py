#Plan work work plan

def display_board(board):
    
    return board

def get_player_move(board, player):

        playerrow = input(f"{player} row: ")
        playercol = input(f"{player} column: ")
        if int(playerrow) <= 4 and int(playercol) <= 4:
            board[int(playerrow) -1][int(playerrow) -1]= player
        else:
            print("Please enter valid positions")
            #reprompt the getplayermove

    # make the space unavailable after filled


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
    #figure out how to get which player it is

def is_draw(board):
    counter = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == "x" or board[row][col] == "o": 
                counter += 1
            return counter

    if counter == 9:
        return True
    else:
        return False
                




def main():
    player = "x"
    player = "o"
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    result = check_winner(board, "X")
    print(result)
    while True:

        print(f"   1   2   3\n1  {board[0][0]} | {board[0][1]} | {board[0][2]}\n  -----------\n2  {board[1][0]} | {board[1][1]} | {board[1][2]}\n  -----------\n3  {board[2][0]} | {board[2][1]} | {board[2][2]}")
        get_player_move(board,player)
        if check_winner(board, player) == True:
            print(f'Congratulations, {player}, you win!')
        
        if is_draw(board) == True:
            break



main()