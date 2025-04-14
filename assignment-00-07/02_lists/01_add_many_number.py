#Write a function that takes a list of numbers and returns the sum of those numbers.

def add_numbers():

    numbers = [1, 2, 3, 4, 5]
    total = 0
    for number in numbers:
        total += number

    print(f"The sum of the numbers is: {total}")

if __name__ == "__main__":    
    add_numbers()