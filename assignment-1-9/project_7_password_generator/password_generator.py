import string
import random

if __name__ == "__main__":
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    plen = int(input("Enter the length of the password: "))

    s= []
    s.extend(list(lower))
    s.extend(list(upper))
    s.extend(list(digits))
    s.extend(list(symbols))

    random.shuffle(s)

    password = random.sample(s, plen)
    password = ''.join(password)
    print("Generated Password: ", password)


