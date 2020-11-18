import os.path

def continue_func():
    input_action= input('Do you want to continue? (y/n): ')
    
    if input_action == 'y': 
        #exec(open('src/storage.py').read())
        os.system('python src/storage.py')
    else: quit()


if os.path.isfile('data.txt'):
    print('\n\nFile already exists \n\n')

    continue_func()
    

    
else: 
    print("\n\nFile doesn't exist\n\n")
    open("data.txt", "w+")
    print('File created successfully')

    continue_func()