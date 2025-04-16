#We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

#Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

#You make a guess, saying your number is either higher than or lower than the computer's number

#If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

#These steps make up one round of the game. The game is over after all rounds have been played.

import random 

MAX_ROUNDS = 5

def main():
    print("Welcome to the High-Low game!")
    print("********************************")
    print("You will play against the computer.")
    print("********************************")

    score = 0
    for i in range(MAX_ROUNDS):
        print("Round:" , i + 1 )
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print("Your number is:", player_number)

        choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
        while choice not in ["higher", "lower"]:
            choice = input("Please enter 'higher' or 'lower': ").lower()


        if choice == "higher":
            if player_number > computer_number:
                print(f"You were right! The computer's number was {computer_number}.")
                score += 1
            else:
                print(f"You were wrong! The computer's number was {computer_number}.")
        if choice ==  "lower":
            if player_number < computer_number:
                print(f"You were right! The computer's number was {computer_number}.")
                score += 1
            else:
                print(f"You were wrong! The computer's number was {computer_number}.")

        print("Your current score is:", score)
        print("********************************")

    #Ending message based on performance
    print("Game Over!")
    print(f"Your Final score is {score}")
    if score >= 4:
        print("Congratulations! You are a High-Low master!")
    elif score >= 2:    
        print("Good job! You did well!")
    elif score >= 0: 
        print("Better Luck next time!")               




if __name__ == "__main__":
    main()
