
def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    left = [i for i in arr if i < pivot]
    right = [j for j in arr if j > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


arr = [3, 15, 4, 22, 1, 0]

print(quicksort(arr))
