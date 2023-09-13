def thirdLargest(arr,n):
    if n<3:
        return -1
    else:
        arr.sort()
        return arr[-3]