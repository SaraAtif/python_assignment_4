#Use Python to calculate the number of seconds in a year, 

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

def main():

    seconds_in_year = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

    print(f"There are {seconds_in_year} seconds in a year!")

if __name__ == "__main__":
    main()    