#Guess My Number

import random

def main():
    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 0 and 99...")

    guess_number = int(input("Enter your guess: "))

    while guess_number != secret_number:
        if guess_number < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()
        guess_number = int(input("Enter new guess: "))

    print(f"congratulations! You guessed the number {secret_number} correctly!")

if __name__ == "__main__":
    main()        

