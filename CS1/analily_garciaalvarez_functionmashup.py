import random


def chorus():
    '''
    prints the chorus of a song

    Args:
    PARAMETER (DATA TYPE): DESCRIPTION
    
    Raises:
    '''
    print('''Y solo mirame con esos ojitos lindos
que con eso yo estoy bien
hoy he vuelto a nacer
    ''')
    
def sing_song():
    print('''Antes de que salga el sol y hunda el acelerador
Que vaya sin frenos y pierda el control
Nada mas seremos dos, tu y yo acariciandonos
En medio del tiempo sin decir adios
          ''')
    chorus()
    print('''Yo no te busque, no
Chocamos en el trayecto 
Con tu alma es la que yo conecto
Tranquila, no tiene que ser perfecto
          ''')
    chorus()


def add(num1, num2):
    '''
    adds two integers

    Args: 
    num1(int): first number
    num2(int): second number
    print: 
    num1+num2(int): sum two numbers
    '''
    print(num1 + num2)
    

def print_list(array):
    '''
    prints every individual element in an array

    Args:
    array(list): a list of words
    print: 
    element(str): a word
    '''
    for element in array:
        print(element)


def in_list(element, array):
    '''
    checks if an element is in an array

    args:
    element(str): a word
    array(list): a list of words
    

    '''
    return element in  array


def is_integer(parameter):
    '''
    checkes if an input is an integer and returns a boolean response

    args:
    parameter(int): a number
    print:
    answer(boolean): true or false
    raises:
    ValueError: is or isn't an integer
    '''
    try:
        int(parameter)
        return True
    except ValueError:
        return False
    

def get_integer():
    '''
    checks if the input is an integer
    args: 
    none

    
    '''
    while True:
        num = input('Enter a number: ')

        if is_integer(num):
            return int(num)
        else:
            print('Enter an integer')


def get_random():
    '''
    gets a random number between two integers inputted by the user

    args:
    none
    print:
    (int): random integer between the two integers
    
    '''
    number1 = get_integer()
    number2 = get_integer()

    if number2 < number1:
        print(random.randint(number2, number1))
    else:
        print(random.randint(number1, number2))

def count_vowels(phrase):
    '''
    counts the vowels in a phrase

    args:
    phrase(str): a phrase
    return:
    count(int): how many vowels there are
    
    '''
    count = 0

    for char in phrase:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(f"There are {count} vowels in your statement")
    return count

def reverse_string(phrase):
    '''
    reverses a phrase the user inputs

    args: 
    phrase(str): a phrase
    return:
    (str): reversed string
    '''
    return phrase[::-1]

def is_palindrome(phrase):
    '''
    checks if a phrase is a palindrome

    args:
    phrase(str): a phrase to check
    prints:
    str: if the phrase is a palindrome, it says that the phrase is a palindrome, and if not, it also says that the phrase is not a palindrome
    
    '''
    return phrase == reverse_string(phrase)

def get_initials(fullname):   
    '''
    gets the initials of a name from a user's input

    args:
    fullname(str): the user's full name
    prints:
    initials(str): the user's initials
    '''
    names = fullname.split()
    initials = ''

    for name in names:
        initials += name[0]
    return initials

def replace_character(phrase, oldchar, newchar):
    '''
    replaces a character that the user chooses

    args:
    phrase(str): full phrase inputted by the user
    oldchar(str): the character the user wants to replace
    newchar(str): the character the user wants to use as a replacement
    prints:
    newphrase(str): the new phrase created
    '''
    new_phrase = ''

    for char in phrase:
        if char == oldchar:
            new_phrase += newchar
        else:
            new_phrase += char
    return new_phrase

def main():
    while True:
        choice = input('''What would you like to do? 
1. sing
2. Add 
3. print list 
4. in list 
7. get random 
8. count vowels
9. reverse string
10. is palindrome
11. get initials
12. replace character 
    ''')

        if choice == '1':
            sing_song()
        elif choice == "2":
            number1 = get_integer()
            number2 = get_integer()
            add(number1, number2)
        elif choice == "3" or choice == "4":
            words = ["sunshine", "beach", "coral", "waves", "sand", "golden"]
            print_list(words)
            print(in_list("sunshine", words))
        elif choice == "7":
            get_random()
        elif choice == "8":
            phrase = input("Enter what you want to count vowels: ").lower()
            count_vowels(phrase)
        elif choice == "9":
            string = input("enter your phrase: ").lower()
            print(reverse_string(string))
        elif choice == "10":
            phrase = input("enter your phrase: ").lower()

            if is_palindrome(phrase):
                print(f'{phrase} is a palindrome')
            else:
                print(f'{phrase} is NOT a palindrome')  
        elif choice == "11": 
            fullname = input("enter your name: ")
            print(f'your initials are {get_initials(fullname)}')
        elif choice == "12":
            phrase = input("enter your phrase: ")
            oldchar = input("enter the character you want to replace: ")
            newchar = input('what do you want to replace it with? ')
            print(f'this is your new phrase: {replace_character(phrase, oldchar, newchar)}') 
    
main()