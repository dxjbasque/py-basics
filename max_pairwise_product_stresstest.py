# Uses python3
import random

# n = int(input())
# a = [int(x) for x in input().split()]
# assert (len(a) == n)


def randomlist(size, maxint):

    randlist = []

    for i in range(0, size):
        randlist.append(random.randint(0, maxint))

    return randlist


def naiveapproach(mylist):
    n = len(mylist)
    result = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if mylist[i] * mylist[j] > result:
                result = mylist[i] * mylist[j]

    return result


def fastapproach(mylist):
    h1 = mylist[0]
    h2 = mylist[1]

    for i in range(1, len(mylist)):
        if mylist[i] > h1:
            h2 = h1
            h1 = mylist[i]
        elif mylist[i] > h2:
            h2 = mylist[i]

    return h1 * h2


testlist = randomlist(random.randint(0, 50000), 99999)
t1 = naiveapproach(testlist)
t2 = fastapproach(testlist)

print(str(t1) + ', ' + str(t2))
if t1 == t2:
    print('Success!!!')
