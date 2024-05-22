**AUTHOR:  MICHAEL KAZEMBE**

**DATE:  21/05/2024**

**COURSE:  CSE 110 - Introduction to Programming**

**INSTRUCTOR:  CHAD OWENS**

# Activity Instructions

#### Overview

Practice using lists and list indexes.

#### Instructions

Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."

Then complete the following:

1. Loop through the items in the regular way (for example, `for thing in the_list`) and display each one to make sure you have the initial list built correctly.
2. Add another loop to go through and print the items in the list, but this time, instead of using the `for ... in` syntax, use an index (for example, `for ... in range`) and then access the item using the index and the square brackets. Print the index in front of the items like so: `0. Milk`
3. Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again.

The following examples show the expected output:

```plaintext

Please enter the items of the shopping list (type: quit to finish):
Item: Milk
Item: Bread
Item: Candy
Item: Carrots
Item: quit

The shopping list is:
Milk
Bread
Candy
Carrots

The shopping list with indexes is:
0. Milk
1. Bread
2. Candy
3. Carrots

Which item would you like to change? 2
What is the new item? Apples

The shopping list with indexes is:
0. Milk
1. Bread
2. Apples
3. Carrots
```
