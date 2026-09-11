import random
while True:
    mylist = ["rock", "paper", "scissors"]
    rps = random.randint(0,2)
    user = input("Rock, paper, or scissors? ").lower()
    
    if user == "rock":
     print(mylist[rps])
     if mylist[rps] == "scissors":
      print("You won!")
     if mylist[rps] == "paper":
      print("You lost!")
     if mylist[rps] == "rock":
      print("Play again")
    elif user == "paper":
     print(mylist[rps])
     if mylist[rps] == "rock":
      print("You won!")
     if mylist[rps] == "scissors":
      print("You lost!")
     if mylist[rps] == "paper":
      print("Play again!")
    elif user == "scissors":
     print(mylist[rps])
     if mylist[rps] == "paper":
      print("You won!")
     if mylist[rps] == "rock":
      print("You lost!")
     if mylist[rps] == "scissors":
      print("Play again!")
    else: 
     print("Please enter 'rock', 'paper', or 'scissors'")