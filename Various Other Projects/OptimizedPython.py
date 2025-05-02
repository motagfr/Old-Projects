def bubbleSort(lst):
    n = len(lst)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                swap = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
            if swap is False:
                break

    return lst


bubbleSort([3, 5, 12, 8, 4, 9])
bubbleSort([1, 2, 3, 4, 5, 6, 7])
