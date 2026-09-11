import random                                                                                                                                                                         #import eandom server
mains = ['cauliflower', 'tilapia fillet',"pork loin", 'salmon','potatoes','three color squash', 'eggplant', 'steak', 'baguette']                                                      #build a list with main dishes
prices = [20,25,28,30,18,20,22,30,20]                                                                                                                                                 #set prices for main dishes
flairs = ['with balsamico','with garlic and olive oil','with minted yogurt','with chutney','salad','with salsa', 'over sticky rice', 'au jus','with basmati rice']                    #build a list for flairs
flairprices = [3, 4, 6, 5, 2, 1, 7, 4, 8]                                                                                                                                             #set prices for flairs
 
while True:                                                                                                                                                                           #forever loop
    try:                                                                                                                                                                              #test
         number = int(input("How many menu items do you need? "))                                                                                                                     #set the input of how many items the customer needs as an integer and name it number
         break                                                                                                                                                                        #break
    except ValueError:                                                                                                                                                                #if the input is not a number
         print('Enter an integer')                                                                                                                                                    #display: enter an integer

costs = []                                                                                                                                                                            #make a list for the costs of the items

for i in range(number):                                                                                                                                                               #for the number in the input
    main_index = random.randint(0, 8)                                                                                                                                                 #set the main index to a random number from 0 to 8
    flair_index = random.randint(0, 8)                                                                                                                                                #set the flair index to a random number from 0 to 8
    print(f'{mains[main_index]} {flairs[flair_index]}, ${prices[main_index]} + ${flairprices[flair_index]} = ${prices[main_index] + flairprices[flair_index]}')                       #display: main + flair, $main cost + $flair cost = $main+flair cost
    costs.append(prices[main_index] + flairprices[flair_index])                                                                                                                       #add the total cost of the meal to the cost list

print(f"Grand total: $ {sum(costs)}")                                                                                                                                                 #display: grand total: sum of costs

