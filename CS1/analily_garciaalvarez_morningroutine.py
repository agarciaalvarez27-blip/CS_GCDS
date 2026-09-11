weather = "rainy"                                                 #set the weather to rainy

print("ALARM")                                                    #display: ALARM

while True:                                                       #forever loop
    snooze = input("snooze? yes or no: ").lower()                 #lowercase user input, ask whether to snooze or not

    if snooze == ("no"):                                          #if the user says no to snoozing,
     hungry = input("Are you hungry? ").lower()                   #ask user if hungry
     break                                                        #break forever loop
    elif snooze == ("yes"):                                       #however, if user says yes to snooze,
     print("5 minutes")                                           #display: 5 minutes
     print("ALARM")                                               #display: ALARM
    else:                                                         #if user does not type yes or no, 
     snooze = input ("please write yes or no: ")                  #ask user to write yes or no

if hungry == ("no"):                                              #if user response to hungry query is no,
     print ("Get ready")                                          #display: get ready

if hungry == ("yes"):                                             #if user response to hungry query is yes,
     print("Make breakfast")                                      #display: Make breakfast
while True:                                                       #forever loop
  breakfast = input("Done with breakfast? ").lower()              #ask user if user is done with breakfast
  if breakfast == ("yes"):                                        #if user response is yes, 
   break                                                          #break forever loop
  if breakfast == ("no"):                                         #if user response is no, 
   print("Finish breakfast")                                      #display: finish breakfast

    


if weather == "sunny":                                            #if set weather is sunny, 
        print("It's sunny out!")                                  #display: it's sunny out!
        sunnychoice = input("Do you want to go to the park or to the beach? ").lower()                         #ask user to choose between park and beach
        if sunnychoice == "go to the park":                                                                    #if user answers park, 
           stroll = input("What a beautiful day in the park! Would you like to go for a stroll? ").lower       #ask user if they want to go for a stroll
           if stroll == "yes":                                                                                 #if the user answers yes
            print("What a beautiful day it is")                                                                #display: what a beautiful day it is
           elif stroll == "no":                                                                                #however if the user answers no
            print("Sit down on the park bench and appreciate the views")                                       #display: sit down on the park bench and appreciate the views
        elif sunnychoice == "go to the beach":                                                                 #instead if user responds "go to the beach"
           splash = input("It's a gorgeous day to be at the beach. Do you want to go in the water? ").lower()  #ask whether the user wants to go in the water
           if splash == "yes":                                                                                 #if the user says yes, 
            print("The water is at the perfect temperature right now :)")                                      #display: the water is the perfect temperature right now
           if splash == "no":                                                                                  #if user answers no
            print("Lie down for a sunkissed tan")                                                              #display: lie down for a sunkissed tan
elif weather == "rainy":                                                                                       #if set weather is rainy,
      print("It's rainy out!")                                                                                 #display: it's rainy out
      rainychoice = input("Do you want to watch a movie or read a book? ").lower()                             #ask if user wants to watch a movie or read a book
      if rainychoice == "watch a movie":                                                                       #if user responds watch a movie, 
        movie = input("Would you like to watch a comedy, romance, action, or thriller? ").lower                #ask if user wants to watch comedy, romance, action, or thriller
        if movie == "comedy":                                                                                  #if user responds "comedy"
         print("Now playing Grown Ups")                                                                        #display: now playing grown ups
        if movie == "romance":                                                                                 #if user answers "romance"
         print("Now playing The Holiday")                                                                      #display: now playing the holiday
        if movie == "action":                                                                                  #if user input is action
         action = input("Do you want to watch Mission Impossible or Tron: Ares? ").lower()                     #ask if user wants to watch mission impossible or tron ares
         if action == ("mission impossible"):                                                                  #if user responds mission impossible
            print("Now Playing Mission Impossible")                                                            #display: now playing mission impossible
         if action == "tron: ares":                                                                            #if user answers tron ares
            print("Now playing Tron: Ares")                                                                    #display: Now playing Tron: Ares
        if movie == "thriller":                                                                                #if user respond "thriller"
           print("Now playing Inception")                                                                      #display: now playing inception
      elif rainychoice == "read a book":                                                                       #if user chooses "read a book"
         book = input("Would you like to read a romance novel, a mystery book, or a magic realism book? ").lower() #ask user if they would like to read romance, mystery, or magic realism
         if book == "romance novel":                                                                           #if user says "romance novel"
            print("Read If He Had Been With Me")                                                               #display: read if he had been with me
         if book == "mystery book":                                                                            #if user says "mystery book"
            print("Read The Cousins")                                                                          #display: read the cousins
         if book == "magic realism":                                                                           #if user says "magic realism"
            print("Read Cien Años de Soledad")                                                                 #display: read cien anos de soledad
      else:                                                                                                    #otherwise
         rainychoice1 = input("please write 'watch a movie' or 'read a book' ")                                #if user replies something else, ask the user to write "watch a movie" or "read a book"
         if rainychoice1 == "watch a movie":                                                                   #repeat previous options through line 95
          movie1 = input("Would you like to watch a comedy, romance, action, or thriller? ").lower             #
          if movie1 == "comedy":                                                                               #
           print("Now playing Grown Ups")                                                                      #
          if movie1 == "romance":                                                                              #
           print("Now playing The Holiday")                                                                    #
         if movie1 == "action":                                                                                #
          action1 = input("Do you want to watch Mission Impossible or Tron: Ares? ").lower()                   #
          if action1 == ("mission impossible"):                                                                #
            print("Now Playing Mission Impossible")                                                            #
         if action1 == "tron: ares":                                                                           #
            print("Now playing Tron: Ares")                                                                    #
         if movie1 == "thriller":                                                                              #
           print("Now playing Inception")                                                                      #
         elif rainychoice1 == "read a book":                                                                   #
          book1 = input("Would you like to read a romance novel, a mystery book, or a magic realism book? ").lower()#
         if book1 == "romance novel":                                                                          #
            print("Read If He Had Been With Me")                                                               #
         if book1 == "mystery book":                                                                           #
            print("Read The Cousins")                                                                          #
         if book1 == "magic realism":                                                                          #
            print("Read Cien Años de Soledad")                                                                 #
elif weather == "snowy":                                                                                       #if set weather is "snowy"
        print("It's snowing!")                                                                                 #display: it's snowing
        snowychoice = input("Do you want to play in the snow or make hot chocolate? ").lower()                 #ask user if they want to play in the snow or make hot cocoa
        if snowychoice == "play in the snow":                                                                  #if user responds play in the snow,
         snowman = input("Do you want to build a snowman? ").lower()                                           #ask user if they want to build a snowman
         if snowman == "yes":                                                                                  #if user says yes, 
            print("Make sure he has a carrot nose!")                                                           #display: make sure he has a carrot nose:
         if snowman == "no":                                                                                   #is user says no, 
            print("Make snow angels as you watch snowflakes falling towards you, each one unique in size and structure, each one equally beautiful as the next.")  # display: make snow angels...
        if snowychoice == "make hot chocolate":                                                                                                                    #if user replies make hot chocolate
         choco = input("Would you like marshmellows? ").lower()                                                                                                    #ask user if they want marshmellows
         if choco == "yes":                                                                                                                                        #if they say yes,
            print('Enjoy your marshmellow hot chocolate while you look out the window to see the most beautiful sight of nature')                                  #display: enjoy your marshmellow hot cocoa...
         if choco == "no":                                                                                                                                         #if user says no, 
            print("I see you enjoy the simple things in life, enjoy your hot cocoa while you look the snow covered treetops")                                      #display: enjoy the simple things in life
#while True:
 #   tired = input("Are you tired? ").lower()
  #  if tired == ("no"):
   #  print("Do your homework")
    # break
    #elif tired == ("yes"):
     #print("Take a nap")

