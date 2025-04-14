#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math

def main():

    side_AB = float(input("\033[1;3m Enter the length of side AB: \033[0m"))
    side_AC = float(input("\033[1;3m Enter the length of side AC: \033[0m"))

    hypotenuse = math.sqrt(side_AB**2 + side_AC**2)

    print(f"The length of BC (the hypotenuse) is: {hypotenuse:.2f}")

if __name__ == "__main__":
    main()    