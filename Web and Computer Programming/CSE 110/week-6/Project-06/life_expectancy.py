"""
AUTHOR: MICHAEL KAZEMBE
DATE: 27/05/2024

life_expectancy.py

A program that analyzes life expectancy data from a CSV file
"""

# STRETCH CHALLENGE
# Added option for user to search by country for min, max and avg life expectancy
# User can identify the country and year for largest drop in life expectancy

import os

file_path = 'life-expectancy.csv'

# Initialize variables to store the overall lowest and highest life expectancy
# values and their corresponding year and country
overall_min_life_expectancy = float('inf')
overall_min_country = ""
overall_min_year = ""

overall_max_life_expectancy = float('-inf')
overall_max_country = ""
overall_max_year = ""

data = []  # To store data for further processing
country_year_data = {}  # To store data organized by country and year

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        # Read the header to find the indices of the relevant columns
        header = file.readline().strip().split(',')
        country_index = header.index('Entity')
        year_index = header.index('Year')
        life_expectancy_index = header.index('Life expectancy (years)')

        for line in file:
            parts = line.strip().split(',')
            country = parts[country_index]
            year = int(parts[year_index])
            try:
                life_expectancy = float(parts[life_expectancy_index])
                data.append((country, year, life_expectancy))

                if country not in country_year_data:
                    country_year_data[country] = []
                country_year_data[country].append((year, life_expectancy))

                # Update overall min and max life expectancy
                if life_expectancy < overall_min_life_expectancy:
                    overall_min_life_expectancy = life_expectancy
                    overall_min_country = country
                    overall_min_year = year

                if life_expectancy > overall_max_life_expectancy:
                    overall_max_life_expectancy = life_expectancy
                    overall_max_country = country
                    overall_max_year = year

            except ValueError:
                continue

    # Display welcome message
    print("=" * 80)
    print("*** WELCOME TO THE LIFE EXPECTANCY ANALYZER ***")
    print("You can enter a year to find the average, minimum, and maximum life expectancy for that year.")
    print("You can also explore other options for more insights.")
    print("To quit, type 'exit'.")
    print("=" * 80)

    # Allow user to input a year and perform analysis for that year
    while True:
        user_input = input("\nEnter the year of interest (or type 'options' for more choices, 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'options':
            print("\nOptions:")
            print(
                "1. Identify the year and country with the largest drop in life expectancy from one year to the next.")
            print("2. Enter a country to get the minimum, maximum, and average life expectancy for that country.")
            option = input("Choose an option (1 or 2): ")

            if option == '1':
                largest_drop = 0
                largest_drop_country = ""
                largest_drop_year = ""

                for country, values in country_year_data.items():
                    values.sort()  # Sort by year
                    for i in range(1, len(values)):
                        drop = values[i - 1][1] - values[i][1]
                        if drop > largest_drop:
                            largest_drop = drop
                            largest_drop_country = country
                            largest_drop_year = values[i][0]

                print(
                    f"\nThe largest drop in life expectancy was {largest_drop:.2f} years in {largest_drop_country} from year {largest_drop_year - 1} to {largest_drop_year}.")

            elif option == '2':
                country_name = input("Enter the country name: ")
                if country_name in country_year_data:
                    life_expectancies = [le for year, le in country_year_data[country_name]]
                    min_life_expectancy = min(life_expectancies)
                    max_life_expectancy = max(life_expectancies)
                    avg_life_expectancy = sum(life_expectancies) / len(life_expectancies)
                    print(f"\nFor {country_name}:")
                    print(f"The average life expectancy is {avg_life_expectancy:.2f}")
                    print(f"The minimum life expectancy is {min_life_expectancy:.2f}")
                    print(f"The maximum life expectancy is {max_life_expectancy:.2f}")
                else:
                    print(f"No data available for the country {country_name}.")
            else:
                print("Invalid option. Please choose 1 or 2.")
            continue

        try:
            user_year = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid year.")
            continue

        total_life_expectancy = 0
        count = 0
        year_min_life_expectancy = 120
        year_min_country = ""
        year_max_life_expectancy = -120
        year_max_country = ""

        for country, year, life_expectancy in data:
            if year == user_year:
                total_life_expectancy += life_expectancy
                count += 1
                if life_expectancy < year_min_life_expectancy:
                    year_min_life_expectancy = life_expectancy
                    year_min_country = country
                if life_expectancy > year_max_life_expectancy:
                    year_max_life_expectancy = life_expectancy
                    year_max_country = country

        # Display results for the user-specified year
        if count > 0:
            average_life_expectancy = total_life_expectancy / count
            print(f"\nFor the year {user_year}:")
            print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
            print(f"The max life expectancy was in {year_max_country} with {year_max_life_expectancy}")
            print(f"The min life expectancy was in {year_min_country} with {year_min_life_expectancy}")
        else:
            print(f"No data available for the year {user_year}")

else:
    print("File not found!")
