"""
AUTHOR: MICHAEL KAZEMBE
DATE: 27/05/2024

data_analysis.py

A program that opens and reads files then parsing strings in python
"""

import os

file_path = "life-expectancy.csv"

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        header = file.readline().strip().split(',')
        life_expectancy_index = header.index('Life expectancy (years)')
        
        lowest_life_expectancy = 120
        highest_life_expectancy = -120
        
        for line in file:
            parts = line.strip().split(',')
            try:
                life_expectancy = float(parts[life_expectancy_index])
                if life_expectancy < lowest_life_expectancy:
                    lowest_life_expectancy = life_expectancy
                if life_expectancy > highest_life_expectancy:
                    highest_life_expectancy = life_expectancy
            except ValueError:
                continue
        
    print(f"Lowest life expectancy: {lowest_life_expectancy}")
    print(f"Highest life expectancy: {highest_life_expectancy}")
else:
    print("File not found!")
