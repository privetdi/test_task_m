import re
from itertools import product

DIGITS = "9876543210"
TARGET = 200


def evaluate(expression):
    return sum(int(term) for term in re.findall(r"[+-]?\d+", expression))


for operators in product(["+", "-", ""], repeat=len(DIGITS) - 1):
    expression = DIGITS[0] + "".join(op + digit for op, digit in zip(operators, DIGITS[1:]))
    if evaluate(expression) == TARGET:
        print(f"{expression}={TARGET}")
