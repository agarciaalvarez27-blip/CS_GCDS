import random
while True:
    int = random.randint(0,10)
    mylist = ["Yes", "No", "Maybe", "Ask again later", "Depends", "Si", "Non", "Oui", "нет", "да", "может быть"]
    input("Ask a question: ")
    print(mylist[int])