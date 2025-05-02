def generateList(n):

    L = list(range(1, n+1))

    missing = random.randint(0, n-1)
    repeating = random.randint(1, n)

    L[missing] = repeating

    random.shuffle(L)

    return L
#####################################################
# Sol 1: Using sort and brute force linear search


def printTwoElements_1(L):

    # sorting the array
    L.sort()
    for i in range(0, len(L) - 1):
        if (L[i] == L[i + 1]):
            repeating = L[i]
            break

    for i in range(1, len(L) + 1):
        found = False
        for j in range(0, len(L)):
            if (i == L[j]):
                found = True
                break

        if (not found):
            missing = i
            break

    return repeating, missing
#####################################################
# Sol 2: Using sort and cleverly sum


def printTwoElements_2(L):

    # sorting the array
    L.sort()
    for i in range(0, len(L) - 1):
        if (L[i] == L[i + 1]):
            repeating = L[i]
            break

    sum_1_n = sum(range(1, len(L) + 1))
    sum_L = sum(L)

    missing = sum_1_n - (sum_L - repeating)

    return repeating, missing
#####################################################


L = [7, 3, 3, 1, 4, 6, 2]
repeating, missing = printTwoElements_1(L)

print("The repeating element is: ", repeating)
print("The missing element is: ", missing)

L = [7, 3, 3, 1, 4, 6, 2]
repeating, missing = printTwoElements_2(L)

print("The repeating element is: ", repeating)
print("The missing element is: ", missing)

#####################################################

L = generateList(1000)

%timeit printTwoElements_1(L)
%timeit printTwoElements_2(L)
