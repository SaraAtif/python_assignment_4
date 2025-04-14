#In this program we show an example of using dictionaries to keep track of information in a phonebook.

def add_contact():
    phonebook = {}
    while True:
        name = input("Enter the nameof the contact: ")
        if name == "":
            break
        number = input("Enter the number of the contact: ")
        phonebook[name] = number
    return phonebook

def read_phonebook(phonebook):
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")

def lookup_contact(phonebook):
    name = input("Enter the name of the contact you want to look up: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Contact not found.")

def main():
    phonebook = add_contact()
    read_phonebook(phonebook)
    lookup_contact(phonebook)

if __name__ == "__main__":
    main()                                