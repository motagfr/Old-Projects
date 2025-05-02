from collections import Counter

L = [1, 2, 3, 4, 5, 5, 7]


def printTwoElements(L):
    length = len(L)
    b = set(L)
    removed_from_L = [k for k, v in Counter(L).items() if v > 1]
    for i in range(1, length):
        if i not in b:
            missing = i
    return removed_from_L[0], missing


y = Counter(L)
y
type(y)
z = Counter("Hello. Today is Thursday.")
z

repeating, missing = printTwoElements(L)
print("The repeated element is", repeating)
print("The the missing element is", missing)
