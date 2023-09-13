def countOfElements(arr,n,x):
    count = 0
    arr.sort()
    for i in range(n):
        if arr[i] <= x:
            count += 1
        else:
            break
    return count