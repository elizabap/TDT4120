#Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands. It iterates over the list, growing a sorted list behind the current location.
#The algorithm: Move item left until you find the correct place. Repeat until end of list.
#https://www.youtube.com/watch?v=8oJS1BMKE64 visualized 
def insertionSort (arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertionSort([5, 2, 4, 6, 1, 3]))

# while loop inside a for loop makes the running time of the algorithm O(n^2)
