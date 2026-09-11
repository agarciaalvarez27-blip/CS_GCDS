#def hello(name):
 #   return(f"hello, {name}")
#hello("Jack")
#hello('steve')
#hello('world')


#print(sum(1))



def is_palindrome(phrase):
    return phrase == phrase[::-1]

def get_initials(fname, lname):   
    return fname[0], lname[0]

def replace_character(oldchar, newchar, phrase1):
    return phrase1.replace(oldchar, newchar)

def main():
    phrase = input("enter your phrase: ").lower()
    if is_palindrome(phrase):
        print(f'{phrase} is a palindrome')
    else:
        print(f'{phrase} is NOT a palindrome')
    fname = input("enter your first name: ")
    lname = input("enter your last name: ")
    print(f'your initials are {fname[0]}{lname[0]}')
    phrase1 = input("enter your phrase: ")
    oldchar = input("enter the character you want to replace: ")
    newchar = input('what do you want to replace it with? ')
    newphrase = phrase1.replace(oldchar, newchar)
    print(f'this is your new phrase: {newphrase}')
main()