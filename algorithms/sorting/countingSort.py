# Counting sort is a sorting algorithm that works by counting the number of elements in an array. Then, it creates a new array with the same length as the original array, and fills it with the number of elements in the original array.
# The running time of Counting sort is O(n + k), where n is the number of elements in the array and k is the number of different values in the array.
# The worst case is O(n^2).

def countingSort(arr, n):
    # create a new array of length n
    count = [0] * n
    # count the number of elements in the array
    for i in arr:
        count[i] += 1
    # create a new array of length n
    result = [0] * len(arr)
    # fill the new array with the number of elements in the original array
    for i in range(n):
        while count[i] > 0:
            result[len(result) - 1] = i
            count[i] -= 1
            result.pop()
    return result
  
print(countingSort([5, 2, 4, 6, 1, 3], 6))

def counting_sort(A,k):
	res = [0]*len(A)
	count = [0 for _ in range(k+1)]
	
	for j in range(0, len(A)):
		count[A[j]] += 1
	for i in range(1, k+1):
		count[i] += count(i-1)
	for j in range(len(A)-1, -1, -1):
		element = A[j]
		res[count[element]-1] = element
		count[element] -= 1

	return res
