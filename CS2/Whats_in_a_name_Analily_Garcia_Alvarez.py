'''
Name: Analily Garcia Alvarez
Description: What's in a Name assignment
Bugs: None known
Date: 9/30/2026
Bonuses:
Log: Initial version: 9/30/2026
'''



import random 



def reverse(name):
    '''
    Reverses the inputted name

    Args: 
    name(str): the user's name
    Return:
    (str):user's reversed name
    Raises:
    '''
    result = ""    
    length = len(name) -1
    while length >= 0:
        result += name[length]
        length = length - 1
    return result

def vowels(name):
    '''
    counts the amount of vowels in the inputted name

    Args:
    name(str): user's name

    returns: 
    int: the total number of vowels
    
    
    '''
    count = 0
    for char in name.lower():
        if char in ["a", "e", "i", "o", "u"]:
            count += 1
    return count
    

def consonant_freq(name):
    '''
    Counts the consonants in the inputted name

    Args:
    name(str): the user's name
    Returns:
    int: total number of consonants 
    '''
    c_count = 0
    for char in name.lower():
        if char in ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]:
            c_count += 1
    return c_count

def first_name(names):
    '''
    Returns the first name

    Args:
    names(list): the user's names in a list
    Returns:
    str: the first word of the name
    '''
    return(names[0])

def middle_name(names):
    '''
    Returns the middle name; anything between the first and the last names

    Args:
    names(list): list of the user's names
    Returns:
    str: middle name(s)

    '''
    middle = ""
    for nam in names[1:-1]:
        middle += nam + " "
    return middle

def last_name(names):
    '''
    Returns the last name

    Args: 
        names(list): the user's full name in a list
    Returns:
        str: the last name or last word of the name

    '''
    return(names[-1])

#def mix(name):

def has_hyphen(name):
    '''
    Checks whether the name contains a hyphen

    Args:
    name(str): the user's full name
    Returns:
    boolean: true is last name has a hyphen, false if not.
    '''
    if "-" in name:
        return True
    else:
        return False

def lowercase(name):
    '''
    Converts a string to lowercase 
    
    Args: 
    name(str): name to convert
    Returns:
    str: lowercase version of the text
    '''
    return(name.lower())

def uppercase(name):
    '''
    Converts a string to uppercase

    Args:
    name(str): name to convert
    Returns:
    str: uppercase version of the text
    '''   
    return(name.upper())

def is_palindrome(name):
    '''
    Checks whether the inputed name(s) is a palindrome

    Args:
    name(str): the user's full name
    Returns:
    boolean: True if the name(s) are a palindrome. 
    '''
    flipped = name[::-1]
    if flipped == name:
        return True
    else:
        return False

def initials(names):
    '''
    Makes initials from the name

    Args: 
    name(str): the user's full name
    Returns"
    str: uppercase initials
    '''
    ini = ""
    for word in names:
        ini += uppercase(word[0])
    return ini


def random_name(name):
    '''
    Mixes up the letters of the name to create a random name

    Args:
    name(str): the user's full name
    Returns:
    str: the letters in a shuffled order
    '''
    chars = list(name)
    random.shuffle(chars)
    newname = ""
    for ch in chars:
        newname += ch
    return newname

def name_sort(name):
    '''
    Returns the letters of the full name as a sorted list

    Args: 
    name(str): the user's full name
    Returns:
    list: the characters sorted
    '''
    chars = []
    for ch in lowercase(name):
        chars.append(ch)
    return sorted(chars)

def is_distinction(names):
    '''
    Identifies if the inputted name includes a distinction

    Args:
    name(str): user's full name
    Returns: 
    boolean: true if the user's name contains a distinction
    '''
    for nam in names:
        if nam in ["Dr.", "Sir", "Esq", "Ph.d"]:
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


   ''').lower()
        if userchoice == "q":
            print("bye!")
            break    
        elif userchoice == "1":
            print(reverse(name))
        elif userchoice == "2":
            print(f"There are {vowels(name)} vowels in your name")
        elif userchoice == "3":
            print(f'There are {consonant_freq(name)} consonants in your name')
        elif userchoice =="4":
            print(f'Your first name is: {first_name(names)}')
        elif userchoice == "5":
            if middle_name(names)== "":
                print("You don't have a middle name")
            else:
                print(f"Your middle name is {middle_name(names)}")
        elif userchoice == "6":
            print (f' Your last name is {last_name(names)}')   
        elif userchoice == "7":
            print(has_hyphen(name))
        elif userchoice == "8": 
            print(lowercase(name))
        elif userchoice == "9":
            print(uppercase(name))
        elif userchoice == "10":
            print(random_name(name))
        elif userchoice == "11":
            print(is_palindrome(name))
        elif userchoice == "12":
            print(name_sort(name))
        elif userchoice == "13":
            print(initials(names))
        elif userchoice == "14":
            print(is_distinction(name))


main()