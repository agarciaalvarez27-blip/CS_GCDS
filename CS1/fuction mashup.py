import random


def chorus():
    '''
    prints the chorus of a song

    Args:
    PARAMETER (DATA TYPE): DESCRIPTION
    Return/Print:
    OUTPUT (DATA TYPE): DESCRIPTION
    Raises:
    ERROR TYPE: REASON
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
    print(num1 + num2)
    

def print_list(array):
    for element in array:
        print(element)


def in_list(element, array):
    return element in  array


def is_integer(parameter):
    try:
        int(parameter)
        return True
    except ValueError:
        return False
    

def get_integer():
    while True:
        num = input('Enter a number: ')

        if is_integer(num):
            return int(num)
        else:
            print('Enter an integer')

def get_random():
    number1 = get_integer()
    number2 = get_integer()

    print(random.randint(number1, number2))

def count_vowels(phrase):
    count = 0

    for char in phrase:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    print(f"There are {count} vowels in your statement")
    return count

def reverse_string(phrase):
    newphrase = phrase(reversed)

        
def main():
    while True:
        choice = input('What would you like to do? 1. sing, 2. Add, 3. print list, 4. in list, 5. is integer, 6. get integer, 7. get random, 8. count vowels ')

        if choice == '1':
            sing_song()
        if choice == "2":
            number1 = get_integer()
            number2 = get_integer()
            add(number1, number2)
        if choice == "3":
         words = ["sunshine", "beach", "coral", "waves", "sand", "golden"]
         print_list(words)
         print(in_list("sunshine", words))
         number = get_integer()
        if choice == "8":
         phrase = str(input("Enter what you want to count vowels: ")).lower
           
         
    
main()

