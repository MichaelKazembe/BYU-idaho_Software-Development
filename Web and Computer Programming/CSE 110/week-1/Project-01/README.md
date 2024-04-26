**AUTHOR:  MICHAEL KAZEMBE**

**DATE:  23/04/2024**

**COURSE:  CSE 110: Introduction to Programming**

**INSTRUCTOR:  CHAD OWENS**

# Project 01: Clever Stories

## Overview

[Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs) are a type of funny story, where a person is asked for words without knowing their context. The words are then placed into a story in a pre-determined format, often resulting in funny statements.

For example, consider prompts for:

* Plural noun
* Verb
* Adjective
* Noun

And a story, such as:

*When it comes to [plural-noun], you would never want to [verb], especially if you encountered a [adjective] [noun].*

A person, may respond to the prompts with the following:

* Plural noun: ducks
* Verb: jump
* Adjective: cold
* Noun: taco

Then the story would read:

*When it comes to ducks, you would never want to jump, especially if you encountered a cold taco.*

## Instructions

For this assignment, you will implement a program that asks the user for a series of words and then displays the story with the user's words inserted into the appropriate places.

The program should begin by asking the user for each of the words. It should then, fill those words into the appropriate places in the story.

To begin, please use the following story:

The other day, I was really in trouble. It all started when I saw a very
*[adjective]* *[animal]* *[verb]* down the hallway. " *[exclamation]* !" I yelled. But all
I could think to do was to *[verb]* over and over. Miraculously,
that caused it to stop, but not before it tried to *[verb]*
right in front of my family.

Make sure to match the punctuation and spacing of the original story exactly (for example, you should not put your words on their own line, they should fit naturally into the story).

Also, make it so that the "exclamation" word is automatically capitalized, because it starts a new sentence.

#### Sample Output

Here is an example of how your program might work:

```plaintext

Please enter the following:

adjective: happy
animal: zebra
verb: sneeze
exclamation: hooray
verb: read
verb: drive

Your story is:

The other day, I was really in trouble. It all started when I saw a very
happy zebra sneeze down the hallway. "Hooray!" I yelled. But all
I could think to do was to read over and over. Miraculously,
that caused it to stop, but not before it tried to drive
right in front of my family. 
```

Another example, where the user typed different values might look like this:

```plaintext

Please enter the following:

adjective: tired
animal: snail
verb: yell
exclamation: oh no
verb: sing
verb: skip

Your story is:

The other day, I was really in trouble. It all started when I saw a very
tired snail yell down the hallway. "Oh no!" I yelled. But all
I could think to do was to sing over and over. Miraculously,
that caused it to stop, but not before it tried to skip
right in front of my family. 
```

#### Showing Creativity and Exceeding Requirements

As stated in the course syllabus, for each of the projects this semester, you'll be provided with the core requirements, or minimum standard expectations. If you complete those requirements, you are eligible for a 93% on the assignment. However, to be eligible for a 100% on the assignment, you will need to do something to show creativity and exceed these core requirements.

For this assignment, here are some ideas of how you might show creativity in addition to the core requirements:

* Consider adding more to the story, including several more words that will be filled in.
* If you have previous experience with topics that we will see later in the semester, consider a sentence that has an "a" or "an" in front of your word, and let the program fill in the right one.
* You can also do anything else you can think of. Remember, the goal here is to experiment with different ideas and to have fun.

Once you have added something extra to the program, you need to add a comment explaining your addition so the grader knows to look for it. Please add a comment at the beginning of the file describing your addition in 1-2 sentences. A comment is a line of code that begins with the pound `#` character.
