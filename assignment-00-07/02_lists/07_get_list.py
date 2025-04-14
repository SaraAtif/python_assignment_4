#Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

def main():
    user_list = []
    while True:
        user_input = input("Enter a value : ")
        if user_input == "":
            break
        user_list.append(user_input)
    print("Your list:", user_list)

if __name__ == "__main__":  
    main()    