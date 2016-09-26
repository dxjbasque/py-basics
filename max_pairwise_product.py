# Uses python3

n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)


h1 = a[0]
h2 = a[1]

for i in range(1, n):
    if a[i] > h1:
        h2 = h1
        h1 = a[i]
    elif a[i] > h2:
        h2 = a[i]

print(h1 * h2)
