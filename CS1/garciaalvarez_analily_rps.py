import random                           #import random server
score = 0                               #set score to zero
name = input("What's your name? ")
print(f'Have fun, {name}')
while True:                             #forever loop
    mylist = ["rock", "paper", "scissors"] #set the list: rock paper scissors to 'mylist'
    rps = random.choice(mylist)              #set a random integer from 0-2 to 'rps'
    user = input("Rock, paper, or scissors? ").lower() #ask the user to input 'rock' 'paper' 'scissors'
    if user == "rock":                  #if the user inputs 'rock'
     print(rps)                 #display a random string 'rock' 'paper' 'scissors'
     if rps == "scissors":      #if the random string is 'scissors'
      print("You won!")                 #display: you won!
      score += 1                        #add one to score
      print(f'your score: {score}')     #display the current score
     if rps == "paper":         #if the random string is 'paper'
      print("You lost!")                #display: you lost!
      score -=1                         #subtract one from score
      print(f'your score: {score}')     #print the current score
     if rps == "rock":          #if the random string is 'rock'
      print("Play again")               #display: play again
      print(f'your score: {score}')     #display the current score
    elif user == "paper":               #else if the user input is 'paper'
     print(rps)                 #display a random sting 'rock' 'paper' 'scissors'
     if rps == "rock":          #if the random string is 'rock'
      print("You won!")                 #display: you won!
      score += 1                        #add one point to the score
      print(f'your score: {score}')     #display the user's current score
     if rps == "scissors":      #if the random string is 'scissors'
      print("You lost!")                #display: you lost!
      score -= 1                        #subract one point from the score
      print(f'your score: {score}')     #display the user's current score
     if rps == "paper":         #if the random string is 'paper'
      print("Play again!")              #display: play again
      print(f'your score: {score}')     #display the user's current score
    elif user == "scissors":            #else if the user input is 'scissors'
     print(rps)                 #display a random sting 'rock' 'paper' 'scissors'
     if rps == "paper":         #if the random string is 'paper'
      print("You won!")                 #display: you won!
      score += 1                        #add one point to the score
      print(f'your score: {score}')     #display the user's current score
     if rps == "rock":          #if the random string is 'rock'
      print("You lost!")                #display: you lost!
      score -= 1                        #subtract one point from the score
      print(f'your score: {score}')     #display the user's current score
     if rps == "scissors":      #if the random string is 'scissors'
      print("Play again!")              #display: play again!
      print(f'your score: {score}')     #display the user's current score
    else:                               #Or else, 
     print("Please enter 'rock', 'paper', or 'scissors'") #display: please enter 'rock', 'paper', or 'scissors'
    