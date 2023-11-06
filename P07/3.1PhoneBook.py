import json


def print_numbers(numbers):

    for number in numbers.values():
        print(number)

def add_number(numbers, name, number):
    numbers.update({name: number})

def remove_number(numbers, name):
    numbers.pop(name)

def lookup_number(numbers, name):
    print(numbers[name])

def load_numbers(numbers, filename):
    #open external file and save conent as new_numbers
    json_file = open('P07/' + filename)
    new_numbers = json.load(json_file)
    #add new_numbers to the existing numbers dictionary
    numbers.update(new_numbers)

def save_numbers(numbers, filename):
    json_object = json.dumps(numbers)
    # open file in write-mode 'w' to make it possible to write data to the file
    with open('P07/' + filename, 'w') as outfile:
        outfile.write(json_object)

def print_menu():
    print ('1. Print all Phone Numbers')
    print ('2. Add a Phone Number')
    print ('3. Remove a Phone Number')
    print ('4. Lookup a Phone Number')
    print ('5. Load numbers')
    print ('6. Save numbers')
    print ('7. Quit')
    print()
phone_book = {}
menu_choice = 0
print_menu()



while True:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        print_numbers(phone_book)

    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        add_number(phone_book, name, phone)

    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        remove_number(phone_book, name)

    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        print(lookup_number(phone_book, name))

    elif menu_choice == 5:
        filename = input("Filename to load: ")
        load_numbers(phone_book, filename)

    elif menu_choice == 6:
        filename = input("Filename to save: ")
        save_numbers(phone_book, filename)

    elif menu_choice == 7:
        break
    else:
        print_menu()