#number = 7
#guess = input("Enter guess: ")
#if guess > number:
#    guess = input("Your guess is too high! Guess again ")
#if guess<=number:
#    guess = input("Your guess is to low! Guess again ")

import random
random.random()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
while True: 
 guess = input("Choose a number 0-9: ")
 if nums == guess:
    print("you got it!")
    break
 else:
    print("Try again!")