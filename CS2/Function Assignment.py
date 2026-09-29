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
    print(name[::-1])

    length = len(name) -1
    while length >= 0:
        print(name[length])
        length = length - 1

def vowels(name):
    count = 0
    for char in name:
        if char in ["a", "e", "i", "o", "u"]:
            count += 1
    print(f'There are {count} vowels in your name.')
    return count

def consonant_freq(name):
    c_count = 0
    for char in name:
        if char in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            c_count += 1
    print(f'There are {c_count} consonants in your name')
    return c_count

def first_name(names):
    print(f'Your first name is {names[0]}')

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
        True
    else:
        False

#def initials(name):

def is_distinction(name):
    if ["Dr.", "Sir", "Esq", "Ph.d"] in name:
        return True
    else: 
        return False



def main():
    name = input("Enter your full name: ")
    names = name.split(" ")

#while True:
   # userchoice = input('''Which would you like to do?
   # 1. Reverse name
    #2. Count vowels
    #3. Count consonants
    #4. Find the index of 
   # ''')
    
    reverse(name)
    vowels(name)
    consonant_freq(name)
    index = name.find(" ")
    first_name(names)
    index2 = name.find(" ", index + 1)
    middle_name(name, index, index2, names)
    last_name(names)
    hyphen(name)
    lowercase(name)
    uppercase(name)
    is_palindrome(name)
    #initials(name)
    is_distinction(name)


main()