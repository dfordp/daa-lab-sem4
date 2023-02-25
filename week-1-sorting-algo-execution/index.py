from numpy import random
import time
import BubbleSort
import InsertionSort
import SelectionSort
import MergeSort
import QuickSort
import QuickSortRandomized

n=int(input("Enter size of required array:"))
A=random.randint(n, size=(n))
print(A)
m=len(A)-1
#Bubble Sort
print("Bubble Sort:")
start=time.time()
BubbleSort.BubbleSort(A)
end=time.time()
print(A)
print((end-start)*10**3,"ms")


#Insertion Sort
print("Insertion Sort:")
start=time.time()
InsertionSort.InsertionSort(A)
end=time.time()
print(A)
print((end-start)*10**3,"ms")

#Selection Sort
print("Selection Sort:")
start=time.time()
SelectionSort.SelectionSort(A)
end=time.time()
print(A)
print((end-start)*10**3,"ms")


#Merge Sort
print("Merge Sort:")
start=time.time()
MergeSort.MergeSort(A,0,m)
end=time.time()
print(A)
print((end-start)*10**3,"ms")

#Quick Sort
print("Quick Sort:")
start=time.time()
QuickSort.QuickSort(A,0,m)
end=time.time()
print(A)
print((end-start)*10**3,"ms")


#Quick Sort Randomized
print("Quick Sort Randomized:")
start=time.time()
QuickSortRandomized.quicksort(A,0,m)
end=time.time()
print(A)
print((end-start)*10**3,"ms")




