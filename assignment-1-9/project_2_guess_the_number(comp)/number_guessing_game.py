import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def set_difficulty(level):
    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS    

def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too Low.")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too High.")
        return attempts - 1
    else:
        print(f"Congratulations! You guessed the number correctly.The answer was {answer}.")


def number_guessing_game():
    print("welcome to the number guessing game!")
    print("I have selected a random number between 1 to 100.")

    answer = random.randint(1, 100)

    level = input("Choose a difficulty level (easy or hard): ").lower()
    attempts = set_difficulty(level)
    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} attempts to guess the number.")
        guessed_number = int(input("Guess a number: "))
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0:
            print("You have run out of attempts. You lose.")
            return
        elif guessed_number != answer:
            print("Guess again.")

number_guessing_game()
