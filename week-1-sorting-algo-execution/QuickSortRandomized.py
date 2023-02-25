from numpy import random

def partition(alist, start, end):
	pivot = random.randint(start, end)
	temp = alist[end]
	alist[end] = alist[pivot]
	alist[pivot] = temp
	pIndex = start
	for i in range(start, end):
		if alist[i] <= alist[end]:
			temp = alist[i]
			alist[i] = alist[pIndex]
			alist[pIndex] = temp
			pIndex += 1
	temp1 = alist[end]
	alist[end] = alist[pIndex]
	alist[pIndex] = temp1
	return pIndex

def quicksort(alist, start, end):
	if start < end:
		pIndex = partition(alist, start, end)
		quicksort(alist, start, pIndex-1)
		quicksort(alist, pIndex+1, end)
	
	return alist


