"""
AUTHOR: MICHAEL KAZEMBE
DATE: 13/11/2024

sentences.py

Program that generates six sentences. Each sentence is
a random combination of a determiner, a noun, and a verb.
The determiner and noun will agree in number (singular or
plural), and the verb will agree in number and tense
(past, present, or future) with the determiner and noun.

"""

import random

def main():
    """Run the main program."""
    # Print six sentences with different combinations of
    # determiners, nouns, and verbs.
    
    print("\nHere are six sentences:\n")
    print(f"a. {make_sentence(1, "past")}")
    print(f"b. {make_sentence(1, "present")}")
    print(f"c. {make_sentence(1, "future")}")
    print(f"d. {make_sentence(2, "past")}")
    print(f"e. {make_sentence(2, "present")}")
    print(f"f. {make_sentence(2, "future")}")
    
    print()

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
        
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_adjective():
    """
    Returns a randomly chosen adjective from the list of adjectives
    
    """
    
    adjectives = [
        "beautiful", "fiery", "vigilant", "charming", "vibrant",
        "adventerous", "new", "resilient", "sophisticated",
        "enthuasistic", "meticulous", "energetic", "tenacious",
        "old", "brilliant", "determined"
    ]
    
    adjective = random.choice(adjectives)
    return adjective


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
        """
        
    if quantity == 1:
        nouns = [
            "bird", "boy", "car", "cat", "child", "dog",
            "girl", "man", "rabbit", "woman"
        ]
    else:
        nouns = [
            "birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"
        ]
        
    noun= random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = [
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        ]
    elif tense == "present":
        if quantity == 1:
            verbs = [
                "drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"
            ]
        else:
            verbs = [
                "drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"
            ]
    else:  # tense is "future"
        verbs = [
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"
        ]
    tense = random.choice(verbs)
    return tense


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    
    prepositons = [
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    
    prepositon = random.choice(prepositons)
    return prepositon


def get_preposition_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.
    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    
    preposition_phrase = f"{preposition} {determiner} {adjective} {noun}"
    return preposition_phrase


def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    
    determiner = get_determiner(quantity)
    # adjective = get_adjective()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    preposition_phrase = get_preposition_phrase(quantity)
    
    sentence = f"{determiner} {noun} {verb} {preposition_phrase}."
    capitalized_sentence = sentence.capitalize()
    return capitalized_sentence
    
main()