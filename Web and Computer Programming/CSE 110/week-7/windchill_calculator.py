"""
AUTHOR: MICHAEL KAZEMBE
DATE: 23/05/2024

windchill_calculator.py

A program that calculates windchill in Fahrenheit using Temperature and wind speed

"""
# START PROGRAM


def calculate_windchill(temperature, wind_speed):
    """
    A function to calculate and return the wind chill based on
    a given temperature and wind speed.
    :param wind_speed: 
    :param temperature:
    :return: f(windchill)
    """
    # Formula to calculate Wind Chill using temperature and wind speed(mph)
    f = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16))\
        + 0.4275 * (temperature * (wind_speed ** 0.16))
    return f


def convert_celsius_to_fahrenheit(celsius):
    """
    a function to convert from Celsius to Fahrenheit
    and return the converted temperature
    :param: Celsius
    :return: Fahrenheit
    """
    # Formula to convert from Celsius to Fahrenheit
    to_fahrenheit = (celsius * (9/5)) + 32
    return to_fahrenheit


def print_results(temperature, wind_speed, wind_chill):
    """
    A function that prints windchill results to the screen
    :param temperature:
    :param wind_speed:
    :param wind_chill:
    :return: print msg to screen
    """
    print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")


def windchill_calculator():
    """ Main Function """
    # WELCOME SCREEN
    print("*** WELCOME TO WIND CHILL CALCULATOR ***")

    while True:
        # PROMPT the user to enter preferred temperature
        temperature = float(input("What is the temperature? "))
        fahrenheit_or_celsius = input("Fahrenheit or Celsius, type 'F' or 'C')?\n ")
        choice = fahrenheit_or_celsius.lower()
        celsius = convert_celsius_to_fahrenheit(temperature)

        # Fahrenheit Choice
        if choice == 'f':
            # Loop through 5 to 60 miles per hour
            for mph in range(5, 61, 5):
                wind_chill = calculate_windchill(temperature, mph)
                print_results(temperature, mph, wind_chill)

        # Celsius Choice
        if choice == 'c':
            # Loop through 5 to 60 miles per hour
            for mph in range(5, 61, 5):
                wind_chill = calculate_windchill(celsius, mph)
                print_results(celsius, mph, wind_chill)
        else:
            print("Invalid input! Enter 'F' for Fahrenheit or 'C' for Celsius")


windchill_calculator()

# END OF PROGRAM




