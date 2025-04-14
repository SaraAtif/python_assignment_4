#We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

def greet(name):
    """Print a greeting to the user."""
    print(f"Hello, {name}!")

def main():
    name = input("What is your name? ")
    greet(name)

if __name__ == "__main__":
    main()        