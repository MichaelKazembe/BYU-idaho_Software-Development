"""
AUTHOR: MICHAEL KAZEMBE

grade_calculator.py 

# Program that determines the letter grade


"""

#  CORE REQUIREMENTS

grade_percent = float(input('What is your grade percentage? '))
if grade_percent >= 90:
    letter_grade = 'A'
elif grade_percent >= 80:
    letter_grade = 'B'
elif grade_percent >= 70:
    letter_grade = 'C'
elif grade_percent >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print()

# STRETCH CHALLENGE 1

last_digit = grade_percent % 10
if last_digit >= 7:
    sign = '+'
elif last_digit < 3:
    sign = '-'
else:
    sign = ' '

# STRETCH CHALLENGE 2

if grade_percent >= 93:
        sign = ' '

# STRETCH CHALLENGE 3

if letter_grade == 'F':
    sign = ' '

is_passed = False
if grade_percent >= 70:
    is_passed = True
else:
    is_passed = False
print()

print(f'Your letter grade is {letter_grade}{sign}')

if is_passed:
    print('Congratulations! You passed the exam.')
else:
    print('Do not be discouraged. With the right amount of effort,')
    print('you will do better next time.')

# End of Program