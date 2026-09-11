'''
Pseudocode for password keeper

parallel arrays: 
websites = []
usernames = []
passwords = []

function add_entry(websites, usernames, passwords):
    ask user for a website
    ask user for a username
    ask user for a password
    save website to websites
    save username to usernames
    save password to passwords

function access_data():
    for i in range(len(websites))
    print "website: websites(i)
    username: usernames(i)
    password: passwords(i)"

function access_website():    
    ask the user which website they want to access
        print "username = usernames(len(userwebsiteinput))"
        print "password = passwords(len(userwebsiteinput))"

main function: 
    while true
    ask user if they want to input data, print their list of websites with their respective usernames and passwords, if they want to access a specific website, or if the user wants to end the program
    if the user says 1: 
        #call add_entry()
    if the user says 2:
        #call function access_data()
    if the user says 3:
        #call function access_website()
    if the user says 4: 
        print bye!
        break
        
'''

import random  # import random library
import string  # import string library
import csv     # import csv library


def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the password keeper

    args:
    websites(list): list of websites inputted
    usernames(list): list of usernames inputted
    passwords(list): list of passwords inputted
    prints:
    check_pw(str): states the strength of the password    
    
    '''
    website = input("Enter website name: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    check_pw(password)
    websites.append(website)
    usernames.append(username)
    passwords.append(password)


def access_data(websites, usernames, passwords):
    '''
    allows user to access their data
    args:
    websites(list): list of websites inputted
    usernames(list): list of usernames inputted
    passwords(list): list of passwords inputted
    prints: 
    website name, username, and password for each entry
    
    '''
    for i in range(len(websites)):
        print(f'''Website: {websites[i]}
Username: {usernames[i]}
Password: {passwords[i]}
        ''')


def access_website(websites, usernames, passwords):
    '''
    allows user to access a specific website's data

    args:
    websites(list): a list of websites
    usernames(list): a list of websites
    passwords(list): a list of websites

    prints:
    the username and password for the inputted website or an error message if it isn't a valid website
    '''    
    web = input("Which website's data would you like to access? ").lower()

    if web in websites:
        print(f"Username: {usernames[websites.index(web)]}")
        print(f"Password: {passwords[websites.index(web)]}")
    else:
        print('That is not a valid website')


def change_user(usernames, websites, passwords):
    '''
    allows user to change a previously inputted username

    args:
    usernames(list): list of all usernames
    websites(list): list of all websites
    passwords(list): list of all passwords

    prints:
    the new account information after the user has been changed or an error message if it isn't a valid username

    '''
    olduser = input("which username would you like to change? ").lower()

    if olduser in usernames: 
        i = usernames.index(olduser)
        usernames[usernames.index(olduser)] = input("what do you want to change it to? ")
        print(f'website: {websites[i]}')
        print(f'username: {usernames[i]}')
        print(f'password: {passwords[i]}')
    else: 
        print("that username does not exist")


def change_password(passwords, websites, usernames):
    '''
    allows user to change a previously inputted password

    args:
    passwords(list): list of all passwords
    websites(list): list of all websites
    usernames(list): list of all usernames

    prints:
    the new account information after the password has been changed or an error message if it isn't a valid password


    '''
    oldpass = input("which password would you like to change? ").lower()
    
    if oldpass in passwords:
        i = passwords.index(oldpass)
        passwords[i] = input("what would you like to change it to? ")
        print(f'website: {websites[i]}')
        print(f'username: {usernames[i]}')
        print(f'password: {passwords[i]}')
    else:
        print("that password does NOT exist")


def generate_password():
    '''
    generates a strong password for the user

    args:
    none

    returns: 
    (str): randomly generated password

    '''
    strpassword = []
    
    for i in range(3):
        strpassword.append(random.choice(string.ascii_lowercase))
        strpassword.append(random.choice(string.ascii_uppercase))
        strpassword.append(random.choice(string.digits))
        strpassword.append(random.choice(string.punctuation))
    random.shuffle(strpassword)
    return "".join(strpassword)


def check_pw(pw):
    '''
    checks the strength of a password given by a user
    
    args:
    pw(str): user inputted password

    prints:
    check_pw(str): lets the user know how strong their password is. (weak, good, strong, very strong)
    '''
    score = 0

    if any(char.isupper() for char in pw):
        score += 1
    if any(char.islower() for char in pw):
        score += 1
    if any(char.isdigit() for char in pw):
        score += 1
    if any(char in string.punctuation for char in pw):
        score += 1

    if score == 1:
        print("your password is weak")
    elif score == 2:
        print("your password is good")
    elif score == 3:
        print("your password is strong")
    elif score == 4:
        print("your password is very strong")


def export_entries(websites, usernames, passwords, filename):
    '''
    exports entries to a csv file

    args:
    websites(list): list of all websites
    usernames(list): list of all usernames
    passwords(list): list of all passwords
    filename(str): name of the file the data is stored to

    prints:
    confirmation message that the file was successfully exported
    '''
    data = zip(websites, usernames, passwords)

    with open(filename, 'w', newline = '') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Web', 'Username', 'Password'])
        writer.writerows(data)
    print(f'Entries exported to {filename}')


def main():
    websites = []       #empty list for websites
    usernames = []      #empty list for usernames
    passwords = []      #empty list for passwords

    password1 = "iLovePasswords123"
    tries = 3

    for i in range(tries):
        userpass = input("please enter your password to access the password keeper: ")

        if userpass == password1:
            break

    if userpass != password1: 
        exit()

    add_entry(websites, usernames, passwords)

    while True:
        userchoice = input('''Which would you like to do? (Enter "q" to quit)
1: Input website data
2: Access all data
3: Access a specific website's data
4: Change a username
5: Change a password   
6: Generate a strong password  
7: Check password strength                                    
8: Export passwords to a csv file
Enter your choice: 
        ''').lower()
        if userchoice == "q":
            print("bye!")
            break
        elif userchoice == "1":
            add_entry(websites, usernames, passwords)
        elif userchoice == "2":
            access_data(websites, usernames, passwords)
        elif userchoice == "3":
            access_website(websites, usernames, passwords)
        elif userchoice == "4":
            change_user(usernames, websites, passwords)
        elif userchoice == "5":
            change_password(passwords, websites, usernames)
        elif userchoice == "6":
            sp_pwd = generate_password()
            print(f'Strong password: {sp_pwd}')
        elif userchoice == "7":
            pw = input("which password strength do you want to check? ")
            check_pw(pw)
        elif userchoice == "8":
            export_entries(websites, usernames, passwords, 'passwords.csv')
main()