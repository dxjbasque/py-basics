# Uses python3
import sys

input = sys.stdin.read()
m, n = map(int, input.split())

n += 2
m += 1

a = [0,1]
for i in range(2, 60):
    a.append((a[i - 1] % 10 + a[i - 2] % 10) % 10)

if n > 60:
    high = a[n % 60]
    low = a[m % 60]
else:
    high = a[n]
    low = a[m]

if high - low < 0:
    print(high - low + 10)
else:
    print(high - low)