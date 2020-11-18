import pickle
import os
import msvcrt

##########################################################################################
#FUNCTIONS
##########################################################################################

def print_overview():

    #Print an overview of all possible actions in the cli
    
    print(" ")
    print("What do you want to do?")
    print("++++++++++++++++++++++++++++++++")
    print("+                              +")
    print("+  1: View URLs                +")
    print("+  2: Add a new URL            +")
    print("+  3: Delete an existing URL   +")
    print("+  4: Quit                     +")
    print("+                              +")
    print("++++++++++++++++++++++++++++++++")
    print(" ")  

    # options = ["View URLs", "Add a new URL", "Delete an existing URL"]
    # divider = "++++++++++++++++++++++++++++++++"
    # print("What do you want to do?")
    # print(divider)
    # for i in range(0, len(options)):
    #     print(f"+  {i+1}: {options[i]}")
    # print(divider)

##########################################################################################

def choose():

    #Choose function to handle the input from the user
    #Endless Loop to run the input several times until it is stopped by an if-Statement
    #Error Exception if invalid characters are inserted

    while True:
        action = input("Please enter one option: ")
        
        try:
            action = int(action)
        except NameError:
            action = 0
        except Exception: 
            action = 0

        if(action > 0 and action < 5):
            break

    return action

##########################################################################################

def display():

    #Print the data from the data file in cli

    for i in range(0, len(urls)):
        print("...............................")
        print(urls[i])

    print("...............................")
    handshake()

##########################################################################################

def add_url(urls):

    #Add an URL the data file
    new_url = input("Please add the link here: ")
    
    urls.append(new_url)
    print("...")
    print("Entry successfully written")

    pickle.dump(urls, open("data.txt", "wb"))

    handshake()

##########################################################################################

def delete_url(urls):

    #Delete a URL from the data file
    index = input("Please insert an index value: ")

    try:
        index = int(index)
        urls.pop(index-1)
        pickle.dump(urls, open("data.txt", "wb"))
        print(" ")
        print("Item successfully deleted")
    except ValueError:
        print("You entered an invalid option")
    except IndexError:
        print("You entered an invalid index number")

    handshake()

##########################################################################################

def handshake():
    print(" ")
    print("Press any key to continue...")
    print(" ")
    msvcrt.getch()
    os.system("cls")

##########################################################################################
#PROGRAM CODE
##########################################################################################

while True:

    urls = pickle.load(open("data.txt", "rb"))

    print_overview() 
    action = choose()

    os.system("cls") 

    if action == 1: display()
    elif action == 2: add_url(urls)
    elif action == 3: delete_url(urls)
    elif action == 4: break


    