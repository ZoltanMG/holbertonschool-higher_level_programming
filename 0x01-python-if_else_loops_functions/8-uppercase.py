#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            valide_letter = chr(ord(letter) - 32)
        else:
            valide_letter = letter
        print('{}'.format(valide_letter), end='')
    print()
