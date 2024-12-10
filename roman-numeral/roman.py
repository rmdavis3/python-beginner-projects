# Roman numerals are made up of seven symbols: I (1), V (5), X (10), L (50), C (100), D (500), and M (1000).
roman_ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VII", "IX"]
roman_tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
roman_hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
roman_thousands = ["", "M", "MM", "MMM"]
roman_dictionary = {"I": 1, "V": 5, "X": 10,
                    "L": 50, "C": 100, "D": 500, "M": 1000}


number = int(input(
    "Please enter an integer from 0 - 3,999 that you want converted to Roman Numeral: "))

roman_numeral = (input(
    "Please enter a roman numeral from I to ? that you want converted to a number: ").upper())
# print(roman_numeral)
x = len(roman_numeral)


def integer_to_roman():
    """converts an integer to a roman numeral"""
    thousands = number//1000 % 10
    hundreds = number//100 % 10
    tens = number//10 % 10
    ones = number//1 % 10
    print(f"{roman_thousands[thousands]}{roman_hundreds[hundreds]}{
        roman_tens[tens]}{roman_ones[ones]}")


def roman_to_integer():
    """converts a roman numeral to an integer"""
    integer = 0
    for index, char in enumerate(roman_numeral[:-1]):
        if roman_dictionary[char] < roman_dictionary[roman_numeral[index+1]]:
            integer -= roman_dictionary[char]
        else:
            integer += roman_dictionary[char]
    # add value of the last character of the user's roman numeral
    integer += roman_dictionary[roman_numeral[-1]]
    print(f"Your Roman Numeral, {roman_numeral}, has a value of {integer}")


roman_to_integer()
