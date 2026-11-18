'''
Name: Analily Garcia Alvarez
Description: Tic Tac Toe Game
Bugs: 
Date: October 22, 2026
Bonuses:
Logs: 

'''
def display_board(board):
    '''
    Description: Displays and returns the board

    Parameters: 
    board(list): a list of lists that include the board modified by the player
    Returns: 
    board(list): a list of lists that the player modifies
    '''
    print(f"   1   2   3\n1  {board[0][0]} | {board[0][1]} | {board[0][2]}\n  -----------\n2  {board[1][0]} | {board[1][1]} | {board[1][2]}\n  -----------\n3  {board[2][0]} | {board[2][1]} | {board[2][2]}")

    return board

def get_player_move(board, player):
    '''
        description: asks the current player (x or o) where they want to position their x or o

        parameters:
        board(list): a list of lists that include the board modified by the players
        player(str): the player, x or o
        returns:
        board(list): modified where the player placed their piece
        except:
        ValueError if the player didn't include an int

    '''
    while True: 
        try: 
            player_row = int(input(f"{player} row: "))
            player_col = int(input(f"{player} column: "))          
            if player_row >= 1 and player_row <= 3 and player_col >=1 and player_col <= 3:
             if board[player_row - 1][player_col - 1] == " ":
                board[player_row -1][player_col - 1]= player
                return
             else:
              print("oops! that space is filled. please enter a valid position")
            else:
             print("Please enter valid positions")
        except ValueError:
            print("Please enter numbers only.")



def check_winner(board, player):
    '''
    description:
    Checks if the board has any winner and returns a boolean if it did

    parameters:
    board(list): list of lists that include the board modified by the players
    player(str): the player, x or o

    returns:
    boolean: True if there exists a winner; false if nobody has won yet or at all
    '''

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



def is_draw(board):
    '''
    description:
    verifies if the game is a drw or not and sends a boolean in return

    parameters:
    board(list): list of list that updates when the user inputs 

    returns:
    Boolean: true or false depending on whether the requirement of the board being full is fulfilled
    
    '''
    counter = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == "x" or board[row][col] == "o": 
                counter += 1


    if counter == 9:
        return True
    else:
        return False
                




def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    turn = 1
    while True:
     
     if turn in range(1, 10, 2):
            player = "x"
     else:
            player = "o"

    
     display_board(board)
     print(f"Player {player}, enter your coordinates:")

     get_player_move(board, player)
     if check_winner(board, player) == True:
         display_board(board)
         print(f'Congratulations, player {player}, you win! ❀')
         while True: 
          is_restart = input("Would you like to play again? ").lower()
          if is_restart == "yes":
                 board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]
                 turn = 1
                 break
          elif is_restart == "no":
                 print("bye!")
                 return
          else:
              print("Please enter yes or no.")
         

        
     elif is_draw(board) == True:
         print("It's a draw! ❀")
         while True:
          is_restart = input("Would you like to play again? ").lower()        
          if is_restart == "yes":
                board = [[' ', ' ', ' '],
                         [' ', ' ', ' '],
                         [' ', ' ', ' ']]
                turn = 1
                break
          elif is_restart == "no":
             print("bye!")
             return          
          else:    
             print("Please enter yes or no.")
     else:
             turn += 1
            


play_game()