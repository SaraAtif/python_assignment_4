#Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

#For example if the user enters the number 2 you would then print:

#4 8 16 32 64 128

def main():
    current_value = int(input("Enter a number: "))
    while current_value < 100:
        current_value *= 2
        print(current_value, end=' ')
    print()  # Print a newline at the end

if __name__ == "__main__":
    main()      