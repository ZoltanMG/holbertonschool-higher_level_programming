#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sum = 0
    if len(sys.argv) > 1:
        for num in sys.argv:
            if num != sys.argv[0]:
                sum += int(num)

    print('{}'.format(sum))
