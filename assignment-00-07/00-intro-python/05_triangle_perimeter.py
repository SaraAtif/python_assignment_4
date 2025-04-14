def main():

    tri_side1 = float(input("\033[1;3m What is the length of the first side of the triangle?:  \033[0m"))
    tri_side2 = float(input("\033[1;3m What is the length of the second side of the triangle?:  \033[0m"))
    tri_side3 = float(input("\033[1;3m What is the length of the third side of the triangle?:  \033[0m"))
      
    tri_perimeter = tri_side1 + tri_side2 + tri_side3

    print(f"The perimeter of the triangle is: {tri_perimeter}")

if __name__ == "__main__":
    main()     