# Radix Sort is a sorting algorithm that works by sorting the numbers in a list by their digits.
def radixSort(arr):
    max_digit = max(arr)
    for i in range(1, max_digit + 1):
        buckets = [[] for _ in range(10)]
        for j in arr:
            buckets[j % 10].append(j)
        arr = [j for bucket in buckets for j in bucket]
    return arr
