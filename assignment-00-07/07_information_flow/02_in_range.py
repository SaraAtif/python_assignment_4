#Implement the following function which takes in 3 integers as parameters:

#def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n, low, high):
    
    if n >= low and n <= high:
        return True
    else:   
        return False

def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: ")) 
    high = int(input("Enter the upper bound: "))
    result = in_range(n, low, high)
    if result:
        print(f"{n} is in the range between {low} and {high}.")
    else:
        print(f"{n} is not in the range between {low} and {high}.")

if __name__ == "__main__":
    main()                