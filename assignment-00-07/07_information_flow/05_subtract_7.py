#Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def subtract_seven(num):    
    num = num - 7
    return num

def main():

    num = 7
    result = subtract_seven(num)
    print(f"This should be 0: {result}")

    # Call the subtract_seven function with an integer argument and print the result
    #result = subtract_seven(10)
    #print(result)  # Expected output: 3

if __name__ == "__main__":
    main()    
