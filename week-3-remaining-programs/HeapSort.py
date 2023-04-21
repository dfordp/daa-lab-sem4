# write code for heap sort

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # check if right child exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap

        # heapify the root
        heapify(arr, n, largest)    

def heapSort(arr):
    n = len(arr)

    # build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # extract elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapify(arr, i, 0)
    return arr

arr = [12, 11, 13, 5, 6, 7]
print(heapSort(arr))
