#There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

#Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

def main():
    fruit_prices = {
        'apple': 0.5,
        'banana': 0.25,
        'orange': 0.75,
        'grape': 0.1,
        'kiwi': 1.5
    }

    total_cost = 0
    for fruit_name in fruit_prices:
        price = fruit_prices[fruit_name]
        quantity = int(input(f"How many {fruit_name}s would you like to buy? "))
        total_cost += price * quantity

    print(f"The total cost of your fruits is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()    
