import random 

options = ["rock", "paper", "scissor"]
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter rock, paper, or scissor: ").lower()
        if player not in options:
            print("Invalid input. Please try again.")
            
    print(f"Player chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("Congratulation! You win!")
    elif player == "paper" and computer == "rock":
        print("Congratulation! You win!")
    elif player == "scissor" and computer == "paper":
        print("Congratulation! You win!")
    else:
        print("Sorry, you lose!") 

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        running = False

        print("Thanks for playing!")
        break
