"""
AUTHOR: MICHAEL KAZEMBE
DATE: 22/05/2024

list_of_numbers.py

"""
# 1. ask user for series of numbers
# 2. append each one to a list
# 3. stop when they enter 0
# 4. compute the sum, or total, of the numbers in the list
# 5. compute the average of the numbers in the list
# 6. find the maximum, or largest, number in the list


# Start program

def list_of_numbers():
    numbers = []
    num = None

    while (num != 0):
        num = int(input("Enter a list of numbers, type 0 when finished: \n"))
        if num == 0:
            break
        else:
            numbers.append(num)

    if (len(numbers) > 0):
        sum_total = 0
        for number in numbers:
            sum_total += number

        number_count = len(numbers)
        average = sum/number_count

        best_num = -1
        for number in numbers:
            if number > best_num:
                best_num = number

        small_num = 99999999999999
        for number in numbers:
            if number > 0 and number < small_num:
                small_num = number

        sorted_numbers = sorted(numbers)
        
        print(f"The Sum is: {sum_total}")
        print(f"The Average is: {average:.3f}")
        print(f"The Largest number is: {best_num}")
        print(f"The Original list: {numbers}")
        print(f"The Sorted list is: {sorted_numbers}")
    
    else:
        print("No Numbers Entered")

list_of_numbers()

# end of program


