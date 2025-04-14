def main():

    temperature = float(input(" \033[1;3m Enter temperature in Fahrenheit: \033[0m"))
    # Convert Fahrenheit to Celsius

    celsius = (temperature - 32) * 5.0 / 9.0
    print(f"Temperature :{temperature}°F = {celsius:.2f}°C")

if __name__ == "__main__":
    main()    