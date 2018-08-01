import json

try:
    with open('birthdaysdata.json', 'r') as file:
        try:
            birthdays = json.load(file)  # to load the data from file
        except json.decoder.JSONDecodeError:
            birthdays = {}  # creating the variable in case the file was empty but existing

except FileNotFoundError:  # creating the file in case it doesn't exist
    with open('birthdaysdata.json', 'w') as file:
        birthdays = {}  # creating the variable dictionary


def add_entry():
    name = input('New name: ').capitalize()
    date = input('{}\'s birthday: '.format(name))
    birthdays[name] = date
    with open('birthdaysdata.json', 'w') as file:  # opening in write mode
        json.dump(birthdays, file)  # saving the new dictionary into a file, overriding the existing one
    print("{} added successfully".format(name))


def find_date():
    name = input('Who\'s birthday you want to know? ').capitalize()
    date = birthdays.get(name, False)
    if date:
        print("{} was born on {}.".format(name, date))
    else:
        print("{} is not in the list.".format(name))


def list_entries():
    print("Current entries in dictionary:")
    if birthdays:
        for name in birthdays.keys():
            print(name.ljust(15), ':', birthdays[name])
    else:
        print("It's empty")


while True:
    what_next = input("\nAdd, Find, Entries or Quit\n").lower()
    if what_next == 'quit':
        print('Bye')
        break
    elif what_next == 'add':
        add_entry()
    elif what_next == 'find':
        find_date()
    elif what_next == 'entries':
        list_entries()
    else:
        print('Invalid action')
