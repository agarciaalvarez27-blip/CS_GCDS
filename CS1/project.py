import random


def chorus():
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
    for vowels in phrase:
        print(f"There are {int(vowels)} in your statement")
        
def main():
    sing_song()
    number1 = get_integer()
    number2 = get_integer()
    add(number1, number2)
    words = ["sunshine", "beach", "coral", "waves", "sand", "golden"]
    print_list(words)
    print(in_list("sunshine", words))
    number = get_integer()
    phrase = str(input("Enter what you want to count vowels: ")).lower
    vowels = ["a", "e", "i", "o", "u"]
main()

