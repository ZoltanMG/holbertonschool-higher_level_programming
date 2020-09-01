#!/usr/bin/python3
for first in range(9):
    for second in range((first + 1), 10):
        if first == 0 and second == 1:
            print('01', end='')
            continue
        print(', {}{}'.format(first, second),end='')
print()
