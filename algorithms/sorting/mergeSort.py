# Merge sort is a divide and conquer algorithm. It works by breaking down the array into smaller sub-arrays, sorting them individually, and then merging them back together.
# The running time of the algorithm is O(n log n), because it breaks the array into smaller sub-arrays, sorts them individually, and then merges them back together.
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

print(mergeSort([5, 2, 4, 6, 1, 3]))


def merge_sort(arr):
  if len(arr) > 1:
    q = len(arr) // 2
    left = arr[:q]
    right = arr[q:]
    return merge(merge_sort(left), merge_sort(right))
  return arr

def merge(right, left):
  result = []
  while len(right) > 0 and len(left) > 0:
    if right[0] < left[0]:
      result.append(right.pop(0))
    else:
      result.append(left.pop(0))
  result.extend(right)
  result.extend(left)
  return result

print(merge_sort([5, 2, 4, 6, 1, 3]))
