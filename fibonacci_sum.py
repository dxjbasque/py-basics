# Uses python3
n = int(input()) + 2
a = [0,1]

for i in range(2, 60):
    a.append((a[i - 1] % 10 + a[i - 2] % 10) % 10)

if n > 60:
    res = a[n % 60]
else:
    res = a[n]

if res == 0:
    print(9)
else:
    print(res - 1)