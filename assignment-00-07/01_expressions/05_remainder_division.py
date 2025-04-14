#Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():

    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))

    quotient = num1 // num2
    remainder = num1 % num2

    print(f"The result of this division is: {quotient} with a remainder of {remainder}.")

if __name__ == "__main__":
    main()    