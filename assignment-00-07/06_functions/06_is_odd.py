def is_odd(value):

    remainder = value % 2
    return remainder == 1

def main():
    for i in range(10 ,20):
        if is_odd(i):
            print(f"{i} is odd")
        else:
            print(f"{i} is even")

if __name__ == "__main__":
    main()                    