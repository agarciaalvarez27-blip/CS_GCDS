import random
name = input("Como tu te llamas? ")
print(f"Good luck {name}!")
words = ["apple", "orange", "banana", "blueberry", "strawberry", "watermelon", "pineapple", "kiwi"]
games = 0
wins = 0
while True:
    print(random.choice(words))
    mylist = list(random.choice(words))
    print(str(random.shuffle(mylist)))
    #str(random.shuffle(list(random.choice(words))))    same as four previous lines
    turns = 5
    while  turns>0:
     print(f'games played: {games}') 
     turns -= 1
     break
    
    
    
    #print(theword = random.choice(words))
    #print(palabra = list(theword))
    #print(random.shuffle(palabra))