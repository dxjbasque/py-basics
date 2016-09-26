# Uses python3
import sys

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())

    numerator = max(a, b)
    denominator = min(a, b)

    while not denominator == 0:
        x = denominator
        denominator = numerator % denominator
        numerator = x

    print((a*b) // numerator)
