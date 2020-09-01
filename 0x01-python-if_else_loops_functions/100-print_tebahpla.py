#!/usr/bin/python3
for cba in reversed(range(98, 123, 2)):
    print('{:c}{:c}'.format(cba, ((cba - 1) - 32)), end='')
