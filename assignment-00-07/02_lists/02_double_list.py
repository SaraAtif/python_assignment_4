#Write a program that doubles each element in a list of numbers.

def main():

    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = []
    for number in numbers:
        doubled_numbers.append(number * 2)
    print("Original numbers:", numbers)
    print("Doubled numbers:", doubled_numbers)

if __name__ == "__main__":
    main()    