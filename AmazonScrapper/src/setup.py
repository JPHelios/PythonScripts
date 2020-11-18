import os.path
import pickle

data_bool = False
description_bool = False

if os.path.isfile('data.txt'): print('data.txt already exists ')  
else: 
    print("\n\ndata.txt doesn't exist")
    open("data.txt", "w+")
    pickle.dump(["Test1"], open("data.txt", "wb"))
    print('data.txt created successfully')
    data_bool = True

if os.path.isfile('description.txt'): print('description.txt already exists')
else: 
    print("description.txt doesn't exist")
    open("description.txt", "w+")
    print('description.txt created successfully')
    description_bool = True

if data_bool == True or description_bool == True:
    print('Initial Dataset: ')
    
    url = []
    name = []

    while True:
        url.append(input("Please provide the url: "))
        print("Url added")

        name.append(input("Please provide a name: "))
        print("Name added")

        again = input("Do you want to add another product? (y/n): ")
        if again == "n": break

pickle.dump(url, open("data.txt", "wb"))
pickle.dump(name, open("description.txt", "wb"))



    # while True:
    #     url = []
    #     name = []
        
    #     url.append(input("Please provide the url: "))
    #     name.append(input("please provide a descriptive name: "))

    #     pickle.dump([url], open("data.txt", "wb"))
    #     pickle.dump([name], open("description.txt", "wb"))

    #     print('Entry was written successfully')
    #     again = input('Do you want to enter another dataset? (y/n): ')

    #     if again == "n": break

os.system('python src/storage.py')
# input_action= input('Do you want to continue? (y/n): ')
# if input_action == 'y': os.system('python src/storage.py')
# else: quit()