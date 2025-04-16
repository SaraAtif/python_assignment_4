#When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

#The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0

def weight_on_planet():
    earth_weight = float(input("Enter a weight on Earth: "))

    planet = input("Enter a Planet: ").lower()

    if planet == "mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "jupiter":   
        gravity_constant = JUPITER_GRAVITY
    elif planet == "saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "uranus":    
        gravity_constant = URANUS_GRAVITY
    elif planet == "neptune":
        gravity_constant = NEPTUNE_GRAVITY
    elif planet == "earth":
        gravity_constant = EARTH_GRAVITY
    else:
        print("Invalid planet name")
        return

    planetry_weight = earth_weight * gravity_constant
    print(f"Your weight on {planet.capitalize()} is: {round(planetry_weight, 2)}")

if __name__ == "__main__":
    weight_on_planet()            