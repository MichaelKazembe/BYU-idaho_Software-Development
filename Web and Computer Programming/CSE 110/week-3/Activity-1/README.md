**AUTHOR:  MICHAEL KAZEMBE**

**DATE:  06/05/2024**

**COURSE:  CSE 110: Introduction to Programming**

**INSTRUCTOR:  CHAD OWENS**

# Activity Instructions

Practice writing programs that compare strings and numbers.

#### Comparing Numbers

Write a program that asks the user for two integers.

Then, write three separate `if`/`else` statements as follows:

* If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".
* If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".
* If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

#### Comparing Strings

Have the program ask the user for their favorite animal. Then write an `if` statement as follows:

* Check to see if the user's favorite animal is the same as *your* favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

##### Hint from Instructor:

When you write the program, you'll "hard code" your favorite animal into the program as the string to check against.

Hard coding just means that you write it directly into the program, sometimes called a *literal* value. Because this value doesn't come from a user or a file or anything, it will always be used, every time the program is run.

Here is an example of the program when it runs:

```plaintext

What is the first number? 4
What is the second number? 3
The first number is greater
The numbers are not equal
The second number is not greater

What is your favorite animal? giraffe
That one is not my favorite.
```

Another example:

```plaintext

What is the first number? 1009
What is the second number? 5250
The first number is not greater
The numbers are not equal
The second number is greater

What is your favorite animal? bear
That's my favorite animal too!
```

And finally, note that in this example, the animal matches, even though the case is different:

```plaintext

What is the first number? 42
What is the second number? 42
The first number is not greater
The numbers are equal
The second number is not greater

What is your favorite animal? BEAR
That's my favorite animal too!
```
