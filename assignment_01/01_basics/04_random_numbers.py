#Print 10 random numbers in the range 1 to 100.
import random 

def main():
    

    print("10 random numbers in the range 1 to 100:")

    for i in range(10):
        number = random.randint(1, 100)
        print(number, end=" ")

if __name__ == "__main__":
    main()        

