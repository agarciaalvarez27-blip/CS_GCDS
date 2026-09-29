'''
Name: Analily Garcia Alvarez
Description: What's in a Name assignment
Bugs: None known
Date: 9/18/2026
Bonuses:
Log: Initial version: 9/18/2026
'''



import random 



def reverse(name):
    '''
    Function:
    Args:
    Parameters:
    Return:
    
    '''
    length = len(name) -1
    while length >= 0:
        return(name[length])
        length = length - 1
        
    return(name[::-1])



def vowels(name):
    count = 0
    for char in name:
        if char in ["a", "e", "i", "o", "u"]:
            count += 1
        return(f'There are {count} vowels in your name.')
    return count

def consonant_freq(name):
    c_count = 0
    for char in name.lower:
        if char in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            c_count += 1
    return c_count

#def first_name(names):
 #   print(f'Your first name is {names[0]}')

def middle_name(name, index, index2, names):
    if names >= 2:
        print(f'Your middle name is: {name[index + 1:index2]}')
    else:
        print("You don't have a middle name")

def last_name(names):
    print(f'Your last name is: {names[-1]}')

#def mix(name):

def hyphen(name):
    if "-" in name:
        return True
    else:
        return False

def lowercase(name):
    print(name.lower)

def uppercase(name):   
    print(name.upper)

def is_palindrome(name):
    flipped = name[::-1]
    if flipped == name:
        return True
    else:
        return False

#def initials(name):

def is_distinction(name):
    if ["Dr.", "Sir", "Esq", "Ph.d"] in name:
        return True
    else: 
        return False



def main():
    name = input("Enter your full name: ")
    names = name.split(" ")

    while True:
        userchoice = input('''Which would you like to do? (enter q to quit)
1. Reverse name
2. Count vowels
3. Count consonants
4. Return first name
5. Return middle name
6. Return last name
7. Return boolean if last name contains a hyphen
8. Convert to lowercase
9. Convert to uppercase
10. Random name (mix up)
11. Is palindrome
12. Full name sorted
13. Initials
14. Identify distinctions


   ''').lower
        if userchoice == "q":
            print("bye!")
            break    
        elif userchoice == "1":
            reverse(name)
        elif userchoice == "2":
            vowels(name)
        elif userchoice == "3":
            consonant_freq(name)
            print(f'There are {c_count} consonants in your name')
        elif userchoice =="4":
            index = name.find(" ")
            first_name(names)
            index2 = name.find(" ", index + 1)
        elif userchoice == "5":
            middle_name(name, index, index2, names)
        elif userchoice == "6":
            last_name(names)   
        elif userchoice == "7":
            hyphen(name)
        elif userchoice == "8": 
            lowercase(name)
        elif userchoice == "9":
            uppercase(name)
        #elif userchoice == "10":
            #random_name(name)
        elif userchoice == "11":
            is_palindrome(name)
        #elif userchoice == "12":
            #namesort(name)
        #elif userchoice == "13":
            #initials(name)
        elif userchoice == "14":
            is_distinction(name)


main()