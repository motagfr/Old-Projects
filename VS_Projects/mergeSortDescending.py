# Python code to sort a list ascendingly using Merge Sort
def mergeSortDescending(lst):
    if len(lst) > 1:

        # Finding the mid of the list
        mid = len(lst)//2

        # Dividing the list elements
        L = lst[:mid]

        # into 2 halves
        R = lst[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp list L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1

    return lst[-1::-1]
