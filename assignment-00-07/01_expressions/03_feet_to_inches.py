#Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. 

inches_per_foot = 12

def main():

    feet = float(input("Enter the number of feet: "))

    inches = feet * inches_per_foot

    print(f"This is {inches} inches.")

if __name__ == "__main__":
    main()    

    


