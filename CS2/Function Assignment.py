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

def first_name(name, index):
    print(f'Your first name is {name[0:index]}')

def middle_name(name, index, index2):
    
    print(f'Your middle name is: {name[index + 1:index2]}')

def last_name(name,index3):
    print(f'Your last name is: {name[index3 + 1:]}')

#def mix(name):
    

def main():
    name = input("Enter your full name: ")
    reverse(name)
    vowels(name)
    consonant_freq(name)
    index = name.find(" ")
    first_name(name, index)
    index2 = name.find(" ", index + 1)
    middle_name(name, index, index2)
    index3 = name.find(" ", index2 + 1)
    last_name(name, index3)


main()