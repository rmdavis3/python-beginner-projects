"""haunted house madlib"""


def madlib():
    """get user input for madlib, generate, and print madlib"""
    noun1 = input("Noun: ")
    adverb1 = input("Adverb: ")
    propernoun_lastname = input("Proper Noun - Last Name: ")
    adj1 = input("Adjective: ")
    noun_number = input("Noun - Number: ")
    adj2 = input("Adjective: ")
    noun_plural = input("Noun - Plural: ")
    adj3 = input("Adjective: ")
    noun_plural2 = input("Noun - Plural: ")
    noun_food = input("Noun - Food: ")
    propernoun_firstname = input("Proper Noun - First Name: ")
    verb_ed1 = input("Verb-ed: ")
    verb_ed2 = input("Verb-ed: ")
    adj_emotion = input("Adjective - Emotion: ")
    verb1 = input("Verb: ")
    adj4 = input("Adjective: ")

    madlib = f"There is a house on my {noun1} that is {adverb1} haunted. \
It's the old {propernoun_lastname} place that's been {adj1} for \
{noun_number} years. I can tell the house is {adj2} because there are \
{noun_plural} and {adj3} {noun_plural2} outside, and it smells like old \
{noun_food}. I heard that a kid named {propernoun_firstname} {verb_ed1} \
inside and never {verb_ed2} back out. My friends and I are {adj_emotion} \
to {verb1} past the house because it's so {adj4}."

    print(madlib)
