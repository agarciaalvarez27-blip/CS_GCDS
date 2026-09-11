import random                      #imports random module
while True:                        #forever loop
    int = random.randint(0,9)      #naming the random integer from 0-9 "int"
    mylist = ["Yes", "No", "Maybe", "Ask again later", "Depends", "Si", "Non", "Oui", "нет", "да"] #naming a list of answers to yes or no questions "mylist"
    while True:                    #forever loop
        user = input("Ask a question: ").lower() #naming the user's input "user" after asking it to ask a question and lowercasing its answer
        word = user.split()        # naming the words in the split user's input "word"
        firstword = word[0]        # naming the first word in the user's input "firstword" (index: 0)
        if firstword == "do":      # if the first word is do, 
            print(mylist[int])     # display: a random word from the list "mylist," selected by the random function
            break                  # break forever loop
        if firstword == "am":      # repeat the same thing from lines 9-11 for all yes or no question answers
            print(mylist[int])
            break
        if firstword == "is":
            print(mylist[int])
            break
        if firstword == "will":
            print(mylist[int])
            break
        if firstword == "does":
            print(mylist[int])
            break
        if firstword == "are":
            print(mylist[int])
            break
        if firstword == "have":
            print(mylist[int])
            break
        if firstword == "can":
            print(mylist[int])
            break
        if firstword == "could":
            print(mylist[int])
            break
        if firstword == "would":
            print(mylist[int])
            break
        if firstword == "may":
            print(mylist[int])
            break
        if firstword == "did":
            print(mylist[int])
            break
        else:                      # if the user inputs anything else, 
            print("Please enter a question!") # display: Please enter a question!