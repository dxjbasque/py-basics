# Uses python3
import sys

input = sys.stdin.read()

n, m = map(int, input.split())
a = [0,1]
cl = 0

for i in range(2, n+1):
    a.append((a[i - 1] % m + a[i - 2] % m)%m)
    if (a[i-1]== 0) & (a[i]== 1):
        a.pop()
        a.pop()
        cl = len(a)
        break

if cl > 0:
    print(a[n % cl])
else:
    print(a[n])