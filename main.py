def insertionSort(arr):
    for i in range(1, len(arr)):
        j=i
        while j > 0 and arr[j-1] > arr[j]:
            tmp = arr[j]
            arr[j]=arr[j-1]
            arr[j-1] = tmp
            j -= 1

arr = [1,23,12,3,12,41,43,14,2,35,24,5,34,5,536,47,65,8,57,8]
insertionSort(arr)
print(arr)