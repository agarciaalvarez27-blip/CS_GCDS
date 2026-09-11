import random
mains = ['cauliflower', 'tilapia fillet',"pork loin", 'salmon','potatoes','three color squash', 'eggplant', 'steak', 'baguette']
prices = [20,25,28,30,18,20,22,30,20]
flairs = ['with balsamico','with garlic and olive oil','with minted yogurt','with chutney','salad','with salsa', 'over sticky rice', 'au jus','with basmati rice']
flairprices = [3, 4, 6, 5, 2, 1, 7, 4, 8]

while True:
    try:
        number = int(input("How many menu items do you need? "))
        break
    except ValueError:
        print('Enter an integer')

costs = []

for i in range(number):
    main_index = random.randint(0, 8)
    flair_index = random.randint(0, 8)
    print(f'{mains[main_index]} {flairs[flair_index]}, ${prices[main_index]} + ${flairprices[flair_index]} = ${prices[main_index] + flairprices[flair_index]}')
    costs.append(prices[main_index] + flairprices[flair_index])

print(f"Grand total: $ {sum(costs)}")
