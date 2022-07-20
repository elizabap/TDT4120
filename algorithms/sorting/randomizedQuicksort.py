# Randomized quicksort is a divide and conquer algorithm that uses randomization to improve the performance of the quicksort algorithm.
# WORST CASE: O(n^2)

import random


def randomizedQuicksort(arr, low, high):
    if low < high:
        pivot = randomizedPartition(arr, low, high)
        randomizedQuicksort(arr, low, pivot - 1)
        randomizedQuicksort(arr, pivot + 1, high)
    return arr

def randomizedPartition(arr, low, high):
    i = random.randint(low, high)
    arr[i], arr[high] = arr[high], arr[i]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


print(randomizedQuicksort([5, 2, 4, 6, 1, 3], 0, 5))
