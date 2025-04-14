#Print 10 random numbers in the range 1 to 100.
#Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:
# random.randint(1, 6)

import random

def main():
    for i in range(10):
        random_number = random.randint(1, 100)
        print(random_number)

if __name__ == "__main__":
    main()          
