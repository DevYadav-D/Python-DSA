def longestName(arr,n):
    temp = '0'
    for i in range(n):
        if len(arr[i]) >= len(temp):
            temp = arr[i]
    return temp