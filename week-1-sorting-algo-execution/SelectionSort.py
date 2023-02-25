def SelectionSort(A):
    for i in range(len(A) - 1):
        smallest_index = i
        
        for j in range(i, len(A)):
            if A[j] < A[smallest_index]:
                smallest_index = j
                
        if i != smallest_index:
            [A[i], A[smallest_index]] = [A[smallest_index], A[i]]


