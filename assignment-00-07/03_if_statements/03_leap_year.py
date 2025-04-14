#Write a program that reads a year from the user and tells whether a given year is a leap year or not.
# The given year must be evenly divisible by 4;
#If the year can also be evenly divided by 100, it is NOT a leap year; unless:
#The year is also evenly divisible by 400. Then it is a leap year.

def main():
    year = int(input("Enter a year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year.")
            else:
                print(year, "is not a leap year.")
        else:
            print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == "__main__":
    main()        