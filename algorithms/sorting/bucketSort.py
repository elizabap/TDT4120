# Bucket sort is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually.
# The average running time of Bucket sort is O(n + k), where n is the number of elements in the array and k is the number of buckets. The worst case is O(n^2).
from algorithms.sorting.insertionSort import insertionSort


def bucketSort(arr):
    # get the maximum and minimum value of the array
    max_value = max(arr)
    min_value = min(arr)

    # create buckets
    buckets = [[] for _ in range(max_value - min_value + 1)]

    # distribute the elements into the buckets
    for i in arr:
        buckets[i - min_value].append(i)

    # sort the buckets
    for i in range(len(buckets)):
        buckets[i] = insertionSort(buckets[i])

    # concatenate the buckets
    result = []
    for i in range(len(buckets)):
        result.extend(buckets[i])

    return result

def bucket_sort(arr):
  n = len(arr)
  B = [[] for _ in range(n)]

  for i in range(n):
    B[int(n*arr[i])].insert(-1, arr[i])

  for j in range(n):
    insertionSort(B[j])

  res = []
  for i in range(len(B)):
    res += (B[i])
    return res
