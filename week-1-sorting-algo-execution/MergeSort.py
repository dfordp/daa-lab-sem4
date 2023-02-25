
def MergeSort(arr, left, right) -> None:
    if left < right:
        mid = left + ((right - left) // 2)
        
        MergeSort(arr, left, mid)
        MergeSort(arr, mid+1, right)
        Merge(arr, left, mid, right)
        
    return


def Merge(arr, left, mid, right) -> None:
    tempList: list[int] = []

    arrayOnePos = left
    arrayTwoPos = mid + 1

    while arrayOnePos <= mid and arrayTwoPos <= right:
        if arr[arrayOnePos] <= arr[arrayTwoPos]:
            tempList.append(arr[arrayOnePos])
            arrayOnePos += 1
        else:
            tempList.append(arr[arrayTwoPos])
            arrayTwoPos += 1
            
    while arrayOnePos <= mid:
        tempList.append(arr[arrayOnePos])
        arrayOnePos += 1
        
    while arrayTwoPos <= right:
        tempList.append(arr[arrayTwoPos])
        arrayTwoPos += 1
        
    currentReplacePosition = left
    
    for num in tempList:
        arr[currentReplacePosition] = num
        currentReplacePosition += 1
