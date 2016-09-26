# Uses python3
import sys

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())

    numerator = int(max(a, b))
    denominator = int(min(a, b))

    while not denominator == 0:
        x = denominator
        denominator = numerator % denominator
        numerator = x

    print(numerator)
