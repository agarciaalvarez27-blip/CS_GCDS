color = "pink"

while True:
    user = input("choose a color").lower()

    if user == color:
        print("you got it!")
        break
    else: 
        print("try again")