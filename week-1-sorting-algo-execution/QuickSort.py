def Partitition(A,lb,ub):
    pivot = A[lb]
    
    i = lb
    
    for j in range(i+1, ub+1):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i], A[lb] = A[lb], A[i]
    
    return i

def QuickSort(A,lb,ub):
    if lb < ub:
        pivot = Partitition(A, lb, ub)
        
        QuickSort(A, lb, pivot - 1)
        QuickSort(A, pivot + 1, ub)



