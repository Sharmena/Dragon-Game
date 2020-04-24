from __future__ import print_function #In certain versions of python, the raw_input command is used in place of input and needs this import. Note that raw_input is not in this code, but may need to be added instead of input.
#You can fix this by using ctrl F, replace, and replacing "input(" with "raw_input(". You will then have to fix this line. If you just replace input with raw_input, it will through off the variable user_input and change it to user_raw_input

inventory = ["torch", "crowbar", "mirror"]                                                                                #This initializes global variables that will be used later in the code
books = ["1R", "Guide to Dungeoneering", "Dragon Family History", "How to Breathe Fire", "How to Play with your Pet Rock"]#The first two are lists while the others are a mixture or strings and integers
room_number = 1                                                                                                           #There was no need for floats
room_two = "dark" #This acts like a boolean but instead of true and false it uses "dark" and "light"
room_two_length = 0
user_input = " "
skull = 3
switch_one = "up" #Another boolean like string with "up" and "down"
switch_two = "up"
switch_three = "up"
attempts = 3
block_one = "black"
block_two = "black"
block_three = "black"
block_four = "black"
restart = 0
skulls_crushed = 0

def cannot_do_that(): #Default string that I call instead of printing the same statement over and over again
    print ("I'm sorry. I don't understand what you are trying to do.")

def command_list(user_input): #If the user puts in "commands" then it will list what they can do in each room
    if user_input.lower() == "commands":
        print("This is what you can do in every room:")
        print("Commands - that is what this is.")
        print("Left, Right, Forward - Helps you navigate each room.")
        print("Inventory - tells you what you have.")
        print("Look - see what is in the room with you.")
        print("Hint - Might help you solve the puzzle in each room.")
        print("Use __ - you can use an item in your inventory or in the room.")
        
def hint(user_input): #Each room has its own hint and appearance as shown in this function and the next one
    if user_input.lower() == "hint":
        if room_number == 1:
            print ("Hint: Just use the key.")
        elif room_number == 2:
            print ("Hint: You may need to check your inventory for some sort of light.")
        elif room_number == 3:
            print("Hint: Look around, then see what item could help you.")
        elif room_number == 4:
            print ("Hint: Use your new ability!")
        elif room_number == 5:
            print ("Hint: Have you tried using the door? I never said it was locked...")
        elif room_number == 6:
            print ("Hint: Look around the other rooms in order to find the answer.")
        elif room_number == 7:
            print ("Hint: Drink me.")  
        
def look(user_input):
    if user_input.lower() == "look": #The .lower() command allows the user to type in statements that aren't caps sensitive. It makes the game a little more flexible
        if room_number == 1:
            print ("In front of you, there is a door")
            print ("To your left there is a bookcase")
            if "key" not in inventory:
                print ("To your right, there is something on the ground")
        elif room_number == 2:
            if room_two == "dark":
                print ("It is too dark to see anything. ")
            else:
                print ("Even with some light, you cannot see far ahead of you")
        elif room_number == 3:
            print("There is something on the walls to your left and right")
            print("In front of you, there is a door")
        elif room_number == 4:
            print ("There is something on the walls to your left and right")
            print ("There is an orb on the ground in front of you")
            print ("There is a distinctly wooden door in the front of the room")
        elif room_number == 5:
            print ("To your right, there is a rock")
            print ("There is something on the wall to your left")
            print ("There is something that look like oil on the ground in front of you. It might be flammable")
            print ("There is a door in the front of the room")
        elif room_number == 6:
            print ("There are torches to either side of you")
            print ("In front of you, there is an ornate door")
        elif room_number == 7:
            print ("In front of you, there is a vial on a pedestal.")
        
def torch(user_input): #The torch and crowbar only have a use in one room but can be called upon in any room to tell you it won't help you
    if user_input.lower() == "use torch":
        if room_number == 1:
            print ("That will not help you here.")
        elif room_number == 3:
            print("That will not help you here.")
        elif room_number == 4:
            print("That will not help you here.")
        elif room_number == 5:
            print("That will not help you here.")
        elif room_number == 6:
            print("That will not help you here.")
        elif room_number == 7:
            print("That will not help you here.")
        
def crowbar(user_input):
    if user_input.lower() == "use crowbar":
        if room_number == 1:
            print ("That will not help you here.")
        elif room_number == 2:
            print("That will not help you here.")
        elif room_number == 4:
            print("That will not help you here.")
        elif room_number == 5:
            print("That will not help you here.")
        elif room_number == 6:
            print("That will not help you here.")
        elif room_number == 7:
            print("That will not help you here.")

def mirror(user_input): #The user starts with a mirror that doesn't progress the game but can help you look at you dragon features
    if user_input.lower() == "use mirror":
        print ("You look into the mirror and see a violet dragon staring back at you. ")
        user_input = input("Would you like to inspect your eyes, mouth, scales, or just go back? ")
        if user_input.lower() == "eyes":
            print ("You look at your emerald eyes and see the slightest sliver of an ebony pupil.")
            print ("You try to blink and watch as an under eyelid closes from the left and right side of your eyes into the center just before your upper eylid envelopes them.")
            print ("The slick movement reminds you of a gecko blinking to the sunlight.")
        elif user_input.lower() == "mouth":
            print ("You open your mouth and observe a row of huge, sharp teeth.")
            print ("It is strange that all of these teeth can fit into your mouth, but that must just be the magic of the spell.")
        elif user_input.lower() == "scales":
            print ("You look at the layered violet scales that now cover your entire body.")
            print ("You have remained the same shape, but your fingers and toes are now claws and the hair on you head has turn inot spikes that go down your entire back.")
            print ("You do have to admit though, you are a pretty good looking dragon.")
        elif user_input.lower() == "go back" or user_input.lower()== "back":
            print ("You look fine. How much can a mirror help you in here anyway?")
        else:
            cannot_do_that()
            
def bookcase(): #This function is for the bookcase in the first room. It iterates through each book in the books list and asks the player if they want to keep it or not. If the player says yes, it is added to their inventory
    if books == []:
        print ("This bookcase is empty.")
    else:
        for book in books:
            print ("On the bookcase you see a book called", book)
            user_input = input("Would you like to take it? ")
            if user_input.lower() == "yes":
                print (book, "has been added to your inventory!")
                inventory.append(book)
                books.remove(book)
            elif user_input.lower()== "no":
                print ("Okay, next.")
            else:
                cannot_do_that() 
                
def using_books(user_input): #This checks to see if the player has each book on them and then allows the player to "read" each one. Some are helpful, but for the most part they are for fun
    if user_input.lower() == "use 1r" and "1R" in inventory:
        print ("You take the book 1R from your inventory.")
        print ("This black book has the number 1 and the letter R scratched into the cover with some sort of red coloring.")
        print ("The pages don't have anything on them except the words 'Find the other hints like me'")
        print ("You put the book back in your inventory.")
    elif user_input.lower() == "use guide to dungeoneering" and "Guide to Dungeoneering" in inventory:
        print ("You take the book Guide to Dungeoneering from your inventory.")
        print ("The title is written in fancy cursive across the cover of the book.")
        print ("The pages are full of hints and instruction on building your own dungeon. It probably won't help you here, but may be fun to look at if you return home.")
        print ("You put the book back in your inventory.")
    elif user_input.lower() == "use dragon family history" and "Dragon Family History" in inventory:
        print ("You take the book Dragon Family History from your inventory.")
        print ("The front cover has an ancient drawing of a bunch of dragons gathered together.")
        print ("The pages are filled with the history of dragons along with a family tree and detailed drawings of each dragon and their family.")
        print ("If you stay as a dragon forever, will this be your new family?")
        print ("You put the book back in your inventory")
    elif user_input.lower()== "use how to play with your pet rock" and "How to Play with your Pet Rock" in inventory:
        print ("You take the book How to Play with your Pet Rock from your inventory")
        print ("The cover has a picture of a reptilian arm petting a rock that doesn't seem to be a pet in any way.")
        print ("The pages have instructions on how to care for your rock, including: pet, rock, ask, and play dead.")
        print ("You put the book back in your inventory.")
    elif user_input.lower() == "use how to breathe fire" and "How to Breathe Fire" in inventory:
        print ("You take the book How to Breathe Fire from your inventory.")
        print ("Step 1: --Think-- about breathing fire.")
        user_input = input("What now? ")
        if user_input.lower() == "think":
            print ("You think about breathing fire. It seems like a pretty good idea.")
            print("Step 2: --become-- the fire")
            user_input = input("What now? ")
            if user_input.lower() == "become":
                print("You become the fire! You think...")
                print("It's kind of warm.")
                print("Step 3: Be sure that you want to breathe fire. Is is necessary? Is now the right time? Is this who you want to be?")
                user_input = input("Are you ready? ")
                if user_input.lower() == "yes":
                    print ("Step 4: Now is the time. All you have to do is breathe.")
                    print ("You are not sure if this has helped or not, but you feel somewhat enlightened. Only time will tell.")
        else:
            print ("Well, I guess this book isn't good enough for you")
        print ("You put the book back in your inventory")
        
def look_inventory(user_input): #This just lets the user see what they have in their inventory
    if user_input.lower() == "inventory":
         print ("This is what you have",inventory[0:])
         
def breathe(user_input): #This command is used in several rooms and has been condensed in this function to save space
    if user_input.lower() == "breathe":
        if room_number == 2:
            print("You manage to light an archaic chandelier that fills the room with light.")
            room_two = "light"
        elif room_number == 3:
            print("You breathe some fire just because you can.")
            print("It didn't help, but it was fun.")
        elif room_number == 6:
            print("That will not help you here.")
        elif room_number == 7:
            print("You are too weak to breathe fire.")
            
def use_skull(user_input):
    if user_input.lower() == "use mysterious skull" or user_input.lower() == "use skull" and "Mysterious Skull" in inventory:
        print("The skull looks part human and part dragon")
        print("It is a great find but when you get home will you put it to rest, put it in a museum, or use it for research?")
            
def all_room_commands(): #Instead of writing each function into each room, this allows one function to be called to save space instead of calling 9
    command_list(user_input)
    using_books(user_input)
    hint(user_input)
    look(user_input)
    mirror(user_input)
    torch(user_input)
    crowbar(user_input)
    look_inventory(user_input)
    breathe(user_input)
    use_skull(user_input)
    

#Now that are the functions and variables are set up, the game can begin 

print("Welcome to the Tomb of the Dragon Child!")
print("Are you ready to solve various puzzles in order to become a human once again?")
user_input = input("Hit enter to Start!")

#The game is put into motion with a forever loop that checks what room you are in to determine what will happen. The game is mostly comprised of if statements working together with input or raw_input to let the player progress
while True:                                                                   
    if room_number == 1:                                                        #Room one
        print ("You are now in the first room.")
        user_input = input("What would you like to do? ")
        if user_input.lower() == "use key" and "key" in inventory:
            print("You have unlocked the door.")
            room_number += 1   
            inventory.remove("key")
        elif user_input.lower() == "breathe": #This command is not revealed until room 4, but it can be used to get through rooms faster if you have to restart
            print("Well, that is one way to get through the room. How did you know you could even do that?")
            room_number += 1
        elif user_input.lower() == "look" or user_input.lower() == "hint" or user_input.lower() == "commands" or user_input.lower() == "inventory" or user_input.lower() == "breathe" or user_input.lower()[0:3] =="use":
            all_room_commands()
        elif user_input.lower()== "forward":
            print ("The door in front of you is locked")
        elif user_input.lower() == "left":
            bookcase()
        elif user_input.lower() == "right": #If you already have a key in your inventory, the key won't appear again
            if not "key" in inventory:
                print ("You see a key. It has been added to your inventory")
                inventory.append("key") #The .append() command adds strings, or items, to your inventory
            else:
                print ("There is nothing there")
        else:
            cannot_do_that() #This function is used frequently and just lets the player know that they typed in an invalid command
    elif room_number == 2:                                                      #Room two
        if room_two == "dark":
            print ("You are now in the second room, it is quite dark in here.")
        else:
            print("You are now in the second room. It is not as dark as it was.")
        user_input = input("What would you like to do? ")
        if user_input.lower() == "use torch" and "torch" in inventory:
            print ("Now you can see a little bit better")
        elif user_input.lower() == "breathe":
            room_two = "light"
            print (room_two)
            print("You manage to light an archaic chandelier that fills the room with light.")
        elif user_input.lower() == "look" or user_input.lower() == "hint" or user_input.lower() == "commands" or user_input.lower() == "inventory" or user_input.lower() == "breathe" or user_input.lower()[0:3] =="use":
            all_room_commands()
        elif user_input.lower() == "forward" and room_two == "dark": #This is the dark room. You cannot move when the room is still dark, but there are 2 ways to make the room light in order to progress
            print ("It is too dark for you to want to move around in here.")
        elif user_input.lower() == "forward" and room_two == "light":
            if room_two_length < 2:
                print ("This is a big room. You will have to keep moving forward") #This just adds variation by making the room longer. If you have to restart, you don't need to go through all 3 sections of the room
                room_two_length += 1
            elif room_two_length >= 2:
                print("The door here is unlocked. On to the next room.")
                room_number += 1
        elif user_input.lower() == "left":
            print ("You see a blue '2B' drawn across the wall")
        elif user_input.lower() == "right":
            if skull == 0: #There are 3 skulls that can be taken, left or destroyed. They won't help the player progress, but are kept track of
                print("There is nothing there.")
            else:
                print ("There is a skull on the floor")
                print ("Upon closer inspection it looks like the skull of a human-dragon hybrid. Perhaps a past adventurer")
                user_input = input("Would you like to crush it, take it, or leave it? ")
                if user_input.lower() == "crush" or  user_input.lower() == "crush it":
                    print("Now their memories will be forgotten forever")
                    print("     But I will remember you as a monster")
                    skull -= 1
                    skulls_crushed += 1
                elif user_input.lower() == "take" or  user_input.lower() == "take it":
                    print ("The mysterious skull has been added to your inventory")
                    print ("Maybe now it can be a part of people's memories forever")
                    inventory.append("Mysterious Skull")
                    skull -= 1
                elif user_input.lower() == "leave" or  user_input.lower() == "leave it":
                    print ("You and the other's who have seen it will always remember")
                else:
                    cannot_do_that()
        else:
            cannot_do_that()
    elif room_number == 3:                                                      #Room three
        print ("You are now in the third room.")
        user_input = input("What would you like to do? ")
        if user_input.lower() == "use crowbar" and "crowbar" in inventory: #The third switch requires the player to use the vrowar from their inventory so that it isn't in plain view
            print ("You found a loose tile that can be lifted up!")
            print ("You see a switch. The switch is now", switch_three)
            user_input = input("Would you like to change it? ")
            if user_input.lower() == "yes":  
                if switch_three == "up":
                    switch_three = "down"
                elif switch_three == "down":
                    switch_three = "up"
                print ("The switch is now", switch_three,)
            elif user_input.lower() == "no":
                print ("The switch is still", switch_three,)
            else:
                cannot_do_that()
        elif user_input.lower() == "look" or user_input.lower() == "hint" or user_input.lower() == "commands" or user_input.lower() == "inventory" or user_input.lower() == "breathe" or user_input.lower()[0:3] =="use":
            all_room_commands()
        elif user_input.lower() == "forward":
            if switch_one == "down" and switch_two == "down" and switch_three == "down": #In order to progress, all three switches have to be changes to down
                print ("The door seems to magically open when you touch it.")
                print ("Those switches seemed to do the trick. On to room four.")
                room_number+= 1
            else:
                print("The door is locked, but there isn't anywhere for a key to fit") #This is just letting the player know that something other than a key is required in this room
        elif user_input.lower() == "right":
            print ("You see a switch. The switch is now", switch_one)  #each switch can be changed or left. It is up to the player
            user_input = input("Would you like to change it? ")
            if user_input.lower() == "yes":
                if switch_one == "up":
                    switch_one = "down"
                elif switch_one == "down":
                    switch_one = "up"
                print ("The switch is now", switch_one)
            elif user_input.lower() == "no":
                print ("The switch is still", switch_one)
            else:
                cannot_do_that()
        elif user_input.lower() == "left":
            print ("You see a switch. The switch is now", switch_two)
            user_input = input("Would you like to change it? ")
            if user_input.lower() == "yes":  
                if switch_two == "up":
                    switch_two = "down"
                elif switch_two == "down":
                    switch_two = "up"
                print ("The switch is now", switch_two)
            elif user_input.lower() == "no":
                print ("The switch is still", switch_two)
            else:
                cannot_do_that()
        else:
            cannot_do_that()
    elif room_number == 4:                                                      #Room four
        print ("You are now in the fourth room.")
        user_input = input("What would you like to do? ")
        if user_input.lower() == "use orb": #This orb introduces breathing fire, but first the player has to go through a set of commands. You could have breathed fire the entire time, but this makes the player aware of the command
            print ("The orb is warm to the touch and is a dark blue with amber exploding from the center.")
            print ("Suddenly, you feel the orb's warmth spreading into you like a fire that just keeps growing.")
            print ("First, you feel a fire in your heart.")
            print ("               Then your mind.")
            print ("                         Then you feel fire running through your veins")
            print ("The feeling seeps into your lungs and you feel like you need to take a deep breath to let the fire out.")
            user_input = input("You have to breathe. ")
            if user_input.lower() == "breathe":
                print ("You cough out some smoke and drop the orb in the process.")
                user_input = input("Breathe again ")
                if user_input.lower()== "breathe":
                    print("A brilliant flame emeges from your mouth and relieves your lungs.")
                    print("You are a dragon. Breathing fire is part of your nature.")
                    if "How to Breathe Fire" in inventory:
                        print("If you ever forget, you have a book that could remind you of your abilities.")
                else:
                    print("The orbs falls out of your hands and clatters to the ground.")
                    print("    You must have done something wrong")
            else:
                print("    You must have done something wrong")
        elif user_input.lower() == "breathe": #The player has to set the door on fire in order to get to the next room
            print("The wooden door turns to ash as your flames engulf it.")
            print("The next room awaits.")
            room_number+=1
        elif user_input.lower() == "look" or user_input.lower() == "hint" or user_input.lower() == "commands" or user_input.lower() == "inventory" or user_input.lower() == "breathe" or user_input.lower()[0:3] =="use":
            all_room_commands()
        elif user_input.lower() == "forward":
            print ("There is a wooden door that doesn't want to open.")
        elif user_input.lower() == "left":
            print("There is a giant, green '3G' scratched into the wall.")
        elif user_input.lower() == "right":
            print("There is a lovely painting of a magenta dragon laying on a couch") #This painting is like the mirror. You can look do different things with it, but it doesn't advance the game
            user_input = input("Would you like to observe further, leave it, or do something else? ")
            if user_input.lower() == "observe" or user_input.lower() == "observe further":
                print ("The magestic dragon is laying across a beige couch and her dark blue eyes seem to stare into your soul.")
                print("Her claws are perfectly filed and while laying on her left side, her monstrous right wing extends towards the ceiling. The other one must be laying behind her.")
                print("The bottom of the picture frame has the name 'Cymrisseon, The Eternal Beauty' in cursive.")
                print("While admiring the brushwork on the painting you hear a velvety smooth voice speak to you")
                print("                   O Brave One, you should get back to your quest.")
            elif user_input.lower()== "leave" or user_input.lower() == "leave it":
                print("You're right. Now isn't the time for artwork and you should return to the task at hand.")
            elif user_input.lower()== "something else" or user_input.lower() == "do something else":
                print("You feel like there might be another way to interact with the painting, but this isn't it.")
            elif user_input.lower() == "breathe":
                print("You try to set the painting on fire, but it doesn't seem to catch.")
                print("The dragon in it seems to be laughing at your ignorance")
                print("                          That was rude")
            else:
                cannot_do_that()
        else:
            cannot_do_that()
    elif room_number == 5:                                                      #Room five
        print ("You are now in the fifth room.")
        user_input = input("What would you like to do? ")
        if user_input.lower() == "use door": #There isn't really a puzzle in this room. The player just needs to use the right command
            print("The door is unlocked. On to the next room.")
            room_number += 1
        elif user_input.lower() == "look" or user_input.lower() == "hint" or user_input.lower() == "commands" or user_input.lower() == "inventory" or user_input.lower() == "breathe" or user_input.lower()[0:3] =="use":
            all_room_commands()
        elif user_input.lower() == "forward":
            print("There is a door.")
        elif user_input.lower() == "left":
            print("You see a yellow '4Y' scratched into the wall")
        elif user_input.lower() == "right":
            print("You see a strange rock") #These commands are all listed in a book earlier in the game. 
            user_input = input("Do you know what to do with it? ")
            if user_input.lower()== "no":
                print("Well, that sucks. Maybe you are missing something.")
            elif user_input.lower() == "yes":
                print("Well then maybe you should do it. Geez.")
            elif user_input.lower() == "pet":
                print("You pet the rock and it makes a gumbling noise. Maybe purring?")
                print ("While petting it, you see that carved into it is its name: Rocknaldo.")
            elif user_input.lower() == "ask":
                print("You ask 'What is Your Quest?'")
                print("It stares at you confused. You would ask more questions, but it probably doesn't have a favorite color.")
            elif user_input.lower() == "rock":
                print("You pick up the rock and rock it in your arms for a while.")
                print("It either fell asleep or didn't. You can't really tell becuase its a rock")
                print("                                                         It just kind of sits there no matter what you do.")
            elif user_input.lower() == "play dead":
                print("You tell the rock to play dead.")
                print("It doesn't move")
                print("Good boy. Uh girl... Rock?")
            else:
                cannot_do_that()
        elif user_input.lower() == "breathe": #This makes sure the player isn't beating every room with fire. It even punishes them for using it too much
            print("You breathe fire and suddenly the whole room erupts in flames.")
            print("The heat is unbearable and you feel you conscienceness slipping.")
            print("Maybe... you can't... solve every problem... with... FIRE...")
            print("")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("You wake with a start. This room looks awful familiar.")
            room_number = 1
            restart+= 1 #This is the first time the player may need to be restarted. Restarts are recorded so that it can be given as one of the end game stats

        else:
            cannot_do_that()
    elif room_number == 6:                                                      #Room six
        if attempts == 0: #The player hs three tries to work with the door and if they don't know the answer, then they won't find it in this room anyway, and restarts the player
            print("You are out of attempts. Time to try again")
            print("")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("You wake with a start. This room looks awful familiar.")
            room_number = 1
            restart+= 1
        else:
            print ("You are now in the sixth room.")
            user_input = input("What would you like to do? ")
            if user_input.lower() == "look" or user_input.lower() == "hint" or user_input.lower() == "commands" or user_input.lower() == "inventory" or user_input.lower() == "breathe" or user_input.lower()[0:3] =="use":
                all_room_commands()
            elif user_input.lower() == "forward": #This four answers are hidden throughout out the game. The first is in the bookcase in room one. Second, left side of room 2. Third, left side of room 4. Fourth, left side of room 5.
                print("A golden door looms before you")
                print("Around the door reads 'You have", attempts, " attempts to complete this challenge. If you fail, you will be sent back to the beginning. Maybe you should pay more attention next time.'")
                print("You move closer and see a block with 4 sections. Each one seems to be able to rotate to different colors. The options are black, red, blue, green, and yellow.")
                print("Maybe if you pick the right order of colors, the door will open.")
                user_input = input("Which color will the first one be? ")
                if user_input.lower()== "black" or user_input.lower()== "red" or user_input.lower()== "blue" or user_input.lower()== "green" or user_input.lower()== "yellow": #Each block starts on black, but can be changed to four other colors
                    print ("click")
                    block_one = user_input.lower()
                    user_input = input("Now the second one: ")
                    if user_input.lower()== "black" or user_input.lower()== "red" or user_input.lower()== "blue" or user_input.lower()== "green" or user_input.lower()== "yellow": 
                        print ("click") 
                        block_two = user_input.lower()
                        user_input = input("The third: ")
                        if user_input.lower()== "black" or user_input.lower()== "red" or user_input.lower()== "blue" or user_input.lower()== "green" or user_input.lower()== "yellow":
                            print("click")
                            block_three = user_input.lower()
                            user_input = input("The last one: ")
                            if user_input.lower()== "black" or user_input.lower()== "red" or user_input.lower()== "blue" or user_input.lower()== "green" or user_input.lower()== "yellow":
                                print("                                     click")
                                block_four = user_input.lower()
                            else:
                                print ("That was not an option!") #This game is very punishing to typoes or wrong commands
                                print ("You just threw away one of your attempts.")
                                attempts -= 1
                        else:
                            print ("That was not an option!")
                        print ("You just threw away one of your attempts.")
                        attempts -= 1
                    else:
                        print ("That was not an option!")
                        print ("You just threw away one of your attempts.")
                        attempts -= 1
                    print("Now for the moment of truth")
                    print("You hesitantly reach for the handle. This will determine your future.")
                    if block_one == "red" and block_two == "blue" and block_three == "green" and block_four == "yellow": #There is only one correct combination of colors that will lead to the next room
                        print("You slowly turn the door handle and") 
                        print("                                     it opens!")
                        print("This must lead to the final room.")
                        room_number +=1
                    else:
                        attempts-=1
                        print("You slowly turn the door handle and")
                        print("                                    it doesn't open")
                        if attempts == 0:
                            print("The door starts to fill with dark green smoke and you hear a gutteral laughter echoing through the darkness as the torches go out.")
                            print("This can't be the end of this tale. This can't...")
                            room_number = 1
                        else:
                            print("Hopefully you won't be stuck in this tomb forever.")
                else:
                    print ("That was not an option!")
                    print ("You just threw away one of your attempts.")
                    attempts -= 1
            elif user_input.lower() == "left":
                print ("An ebony torch burns on the wall. Instead of orange, the fire burns green, blue, and purple.")
            elif user_input.lower() == "right":
                print ("An ebony torch burns on the wall. Instead of orange, the fire burns green, blue, and purple.")
            else:
                cannot_do_that()
    elif room_number == 7:                                                      #Room seven
        print ("You are now in the last room. You feel very weak. This half dragon half human form won't hold much longer.") #The player just has to drink or use the vial in order to beat the game
        user_input = input("What would you like to do? ")
        if user_input.lower() == "use vial" or user_input.lower() == "drink vial" or user_input.lower() == "drink":
            print("You approach the vial and pick it up. It is a viscous green fluid.")
            print("Upon opening it, the stench overwhelms you and you wish this wasn't your only option.")
            print ("Reluctantly, you drink it. It tastes... kind of minty.")
            print ("After a few moments, you feel your scales retracting along with your claws. It hurts, but seems to be working.")
            print ("You take out your mirror and watch as your features fade back into the ones you knew so well.")
            print("You find that you are no longer in the dungeon, but outside of it.")
            print("You look into the entrance, but this time, you know better and start to make your way home.")
            break #This breaks the forever loop and goes to the end game
        elif user_input.lower() == "look" or user_input.lower() == "hint" or user_input.lower() == "commands" or user_input.lower() == "inventory" or user_input.lower() == "breathe" or user_input.lower()[0:3] =="use":
            all_room_commands()
        if user_input.lower() == "forward":
            print ("There is no forward. This is all that remains.")
        else:
            cannot_do_that()
    else:
        print ("There may be a problem. You will have to restart your adventure. ")
        break
        
user_input = input("Hit enter to continue.") #This is just a pause to let the player read what happened before ending the game

print("            _")  #Here is a thumbs up I found online for fun 
print("           /(|")
print("          (  :")
print("         __\  \  _____")
print("       (____)  `|")
print("      (____)|   |")
print("       (____).__|")
print("        (___)__.|_____")

print("Congratulations! You made it out") #These are final statistics to let the player know how they did. Not overall helpful, but different players can compare their final stats if they remember them
print("Here are some final stats:")
print("Inventory:", inventory[0:])
print("Amount of times restarted:", restart)
print ("Books left in bookcase:", books)
print("Skulls crushed:", skulls_crushed)
if skulls_crushed >0:
    print ("             You monster.")