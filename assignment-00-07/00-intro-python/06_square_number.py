def main():

    num = int(input("\033[1;3m Type a number to see its square: \033[0m"))

    
    square = num ** 2

    print(f"{num} squared is {square}")

if __name__ == "__main__":
    main()    