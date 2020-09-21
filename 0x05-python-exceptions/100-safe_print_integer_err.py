#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as v_err:
        sys.stderr.write("Exception: {}\n".format(v_err))
        return False
    except TypeError as t_err:
        sys.stderr.write("Exception: {}\n".format(t_err))
        return False

    return True
