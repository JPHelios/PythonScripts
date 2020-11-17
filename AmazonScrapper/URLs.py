import pickle
import os

os.system("cls")

#Print already existing URLs
urls = pickle.load(open("data.txt", "rb"))
for i in range(0, len(urls)):
    print("...............................")
    print(urls[i])

print("...............................")

for i in range(0,3):
    print(" ")

#Choose action
print("What do you want to do?")
print("++++++++++++++++++++++++++++++++")
print("+                              +")
print("+  1: View URLs                +")
print("+  2: Add a new URL            +")
print("+  3: Delete an existing URL   +")
print("+                              +")
print("++++++++++++++++++++++++++++++++")
print(" ")

def choose():

    while True:
        action = input("Please enter one option: ")
        
        try:
            action = int(action)
        except NameError:
            action = 0
        except Exception: 
            action = 0

        if(action == 1 or action == 2 or action == 3):
            break

    return action


action = choose()
print(f"You choose: {action}" )