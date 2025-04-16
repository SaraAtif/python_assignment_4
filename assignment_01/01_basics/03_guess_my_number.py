import random
def main():
    answer = random.randint(1, 99)

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 0 to 99.")
    is_running = True 
    while is_running:
        guess = int(input("Guess a number: "))
        if guess < answer:
            print("Your guess is too low.")
        elif guess > answer:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed it right. The number was {answer}.")
            is_running = False
        
    print("Thank you for playing!")


    
if __name__ == "__main__":
    main()            


