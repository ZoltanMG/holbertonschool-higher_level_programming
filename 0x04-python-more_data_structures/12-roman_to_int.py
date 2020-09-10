#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num_roman = 0
    for i in range(len(roman_string)):
        if roman_string[i] in numbers:
            if i == 0:
                num_roman += numbers[roman_string[i]]
            elif numbers[roman_string[i]] > numbers[roman_string[i - 1]]:
                    num_roman -= numbers[roman_string[i - 1]] * 2
                    num_roman += numbers[roman_string[i]]
            else:
                num_roman += numbers[roman_string[i]]
        else:
            return 0
    return num_roman
