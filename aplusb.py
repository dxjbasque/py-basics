# Uses Python3
# Given two digits a and b, find a+b.
# Problem. Given two digits a and b, find a+b.
# Input format. The first line of the input contains two integers a and b (separated by a space).
# Constraints. 0<=a,b<=9.
# Output format. Output a+b.

import sys

input = sys.stdin.read()
tokens = input.split()

a = int(tokens[0])
b = int(tokens[1])

if 0 <= a <= 9 and 0 <= b <= 9:
    print(a + b)
else:
    sys.stderr.write("Constraint Violation")
