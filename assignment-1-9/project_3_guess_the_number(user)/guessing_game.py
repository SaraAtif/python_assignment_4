import random


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 50.")

    answer = random.randint(1, 50)

    levels =input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if levels == "easy":
        attempts = 10
        print("You have 10 attempts to guess the number.")

    elif levels == "hard":
        attempts = 5
        print("You have 5 attempts to guess the number.")

    attempts = 0    

    while True:
        guess = int(input("Make a guess: "))
        attempts += 1

        if guess < answer:
            print("Too low.")
        elif guess > answer:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number {answer} in {attempts} attempts.")
            break

        if attempts == 10 and levels == "easy":
            print("You've run out of attempts. Game over!")
            break
        elif attempts == 5 and levels == "hard":
            print("You've run out of attempts. Game over!")
            break   

play_game()        



            


