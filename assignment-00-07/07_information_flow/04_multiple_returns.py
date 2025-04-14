#There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

#To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

#Asks the user for their first name and stores it in a variable

#Asks the user for their last name and stores it in a variable

#Asks the user for their email address and stores it in a variable

#Returns all three of these pieces of data in the order it was asked

#You can return multiple pieces of data by separating each piece with a comma in the return line.

def get_user_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    
    return first_name, last_name, email

def main():
    user_data = get_user_data()
    print("Here is the data you entered:")
    print(f"First Name: {user_data[0]}")
    print(f"Last Name: {user_data[1]}")     
    print(f"Email: {user_data[2]}")
    print("Thank you for signing up!")

if __name__ == "__main__":  
    main()        