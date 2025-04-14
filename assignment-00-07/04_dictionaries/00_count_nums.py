#This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

def get_user_num():
    number =[]
    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            break

        num = int(user_input)
        number.append(num)

    return number

def count_numbers(numbers):
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return count

        
def print_count(count):
    for num in count:
        print(f"{num} appears {count[num]} times")

def main():
    numbers = get_user_num()
    count = count_numbers(numbers)
    print_count(count)

if __name__ == "__main__":
    main()            
