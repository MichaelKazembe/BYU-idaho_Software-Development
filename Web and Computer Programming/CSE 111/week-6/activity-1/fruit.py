"""
AUTHOR: MICHAEL KAZEMBE
DATE: 11/12/2024

fruit.py

A program that demonstrates object oriented programming
by modifying a list.

"""

def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    # Reverse and print the list.
    fruit_list.reverse()
    print(f"reverse: {fruit_list}")
    
    # Append "Orange" to the list and print it.
    fruit_list.append("orange")
    print(f"append: {fruit_list}")
    
    
    # Locate "apple" in the list
    # Insert "cherry" before "apple" and print the list.
    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(f"insert: {fruit_list}")
    
    # Remove "banana" from the list and print it.
    fruit_list.remove("banana")
    print(f"remove: {fruit_list}")
    
    # Pop the last item from the list
    # and print the popped item and the list.
    popped_item = fruit_list.pop()
    print(f"popped item: {popped_item}")
    
    # Sort the list and print it.
    fruit_list.sort()
    print(f"sorted list: {fruit_list}")
    
    # Clear the list and print it.
    fruit_list.clear()
    print(f"cleared list: {fruit_list}")
    
    
if __name__ == "__main__":
    main()