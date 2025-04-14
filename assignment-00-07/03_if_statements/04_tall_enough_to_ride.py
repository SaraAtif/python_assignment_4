#Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

#In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like
#For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops.

max_height = 50

def main():
    while True:
    
        height= input("How tall are you? ")
        
            
        if height >= max_height:
            print("You are tall enough to ride!")
        else:
            print("You are not tall enough to ride.")

        if height == "":
            break    


if __name__ == "__main__":
    main()


            
                    

            
            