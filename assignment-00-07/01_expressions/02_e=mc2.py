#Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:


def main():

   mass = float(input("\033[1;3m Enter mass in kilograms: \033[0m"))

   c = 299792458  # Speed of light in m/s
   
   E = mass * c**2  # E = mc^2

   print("e = mc^2")
   print(f"m = {mass} kg")
   print(f"c = {c} m/s")

   print(f"{E} + Joules of energy!")

if __name__ == "__main__":
    main()   

