import pickle

url = []
name = []

print('Initial Dataset')
print(url)
while True:
    url.append(input('Testinput: '))

    print(url)

    again = input("Do you want to add another product? (y/n): ")
    if again == "n": break

print(len(url))
pickle.dump([url], open("data.txt", "wb"))