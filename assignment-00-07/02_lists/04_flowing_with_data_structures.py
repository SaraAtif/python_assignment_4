def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)


def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("Before adding copies:", my_list)
    add_three_copies(my_list, message)
    print("After adding copies:", my_list)

if __name__ == "__main__":
    main()            

