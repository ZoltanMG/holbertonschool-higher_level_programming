#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    if type(text) != str:
        raise TypeError('text must be a string')

    for i in range(len(text)):
        if i == 0 or i == (len(text) - 1):
            if text[i] != ' ':
                print('{}'.format(text[i]), end='')
        elif text[i - 1] in ('.', '?', ':'):
            if text[i] == ' ':
                print('\n')
            else:
                print('\n{}'.format(text[i]))
        else:
            print('{}'.format(text[i]), end='')
