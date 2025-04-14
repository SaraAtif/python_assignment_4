#Simulate rolling two dice, and prints results of each roll as well as the total.

import random

num_Of_dice =6
def main():

    # Simulate rolling two dice
    die1 = random.randint(1, num_Of_dice)
    die2 = random.randint(1, num_Of_dice)

    # Calculate the total of the two dice
    total = die1 + die2

    # Print the results
    print(f"first die: {die1}")
    print(f"second die: {die2}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()    
