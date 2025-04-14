#Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

#Prompt the user to enter a fruit ("Enter a fruit: ")

#Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

#Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

#Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.


def num_in_stock(fruit):
    if fruit == "apple":
        return 5
    elif fruit == "banana":
        return 12
    elif fruit == "orange":
        return 6
    elif fruit == "grapes":
        return 50
    else:
        return 0

def main():
    fruit = input("\033[1;3m Enter a fruit: \033[0m")
    stock = num_in_stock(fruit)
    
    if stock == 0:
        print("This fruit is not in stock.")
        
    else:
        print(f"This fruit is in stock! Here is how many: {stock}")     

if __name__ == "__main__":
    main()                           