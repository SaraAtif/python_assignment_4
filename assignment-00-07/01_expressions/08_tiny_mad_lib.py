#Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def mad_libs():

    adjective = input("\033[1;3m Please type an adjective and press enter: \033[0m")
    noun = input("\033[1;3m Please type a noun and press enter: \033[0m")
    verb = input("\033[1;3m Please type a verb and press enter: \033[0m")

    sentence =f"Once upon a time, there was a {adjective} {noun} who loved to {verb}."

    print(sentence)

if __name__ == "__main__":
    mad_libs()    