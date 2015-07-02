## from http://stackoverflow.com/questions/11266068/python-avoid-new-line-with-print-command

from __future__ import print_function
import sys

def test(func, expected):
    if func == expected:
        sys.stdout.write(".")
    else:
        sys.stdout.write("F")

# This works with the from __future__ import print_function
def test_new(func, expected):
    if func == expected:
        print(".", end="")
    else:
        print("F", end="")

