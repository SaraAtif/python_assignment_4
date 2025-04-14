#Write a function that takes two numbers and finds the average between the two.

def average(num1, num2):

    return (num1 + num2) / 2

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    avg = average(num1, num2)

    print(f"The average of {num1} and {num2} is {avg}")

if __name__ == "__main__":
    main()        