def swapKth(arr,n,k):
    arr[k-1], arr[-k] = arr[-k], arr[k-1]
    return arr