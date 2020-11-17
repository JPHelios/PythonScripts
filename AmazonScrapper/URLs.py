import pickle
import os

os.system("clr")

#Print already existing URLs
urls = pickle.load(open("names.txt", "rb"))
for i in range(0, len(urls)):
    print("...............................")
    print(urls[i])

for i in range(0,5):
    print(" ")

#Choose action
print("What do you want to do?")
print("++++++++++++++++++++++++++++++++")
print("+                              +")
print("+  1: Add a new URL            +")
print("+  2: Delete an existing URL   +")
print("+                              +")
print("++++++++++++++++++++++++++++++++")
print(" ")

def choose():
    action = input("Please enter one option: ")


    while((action != 1) and (action != 2)):
        action = input("Please enter one option: ")
        print("wrong number")

    return action()
    # if(action == 1):
    #     return action
    # elif(action == 2):
    #     return action
    # else: 
    #     choose()

    



action = choose()



print(f"You choose: {action}" )