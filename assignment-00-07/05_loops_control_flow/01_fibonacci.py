#Write a program to print terms in the Fibonacci sequence up to a maximum value.
#Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!).

max_value = 10000

def main():
    current_value = 0
    next_value = 1

    while current_value < max_value:
        print(current_value)
        term_after_next = current_value + next_value
        current_value = next_value
        next_value = term_after_next

if __name__ == "__main__":
    main()        