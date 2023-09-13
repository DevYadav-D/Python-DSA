def leftElement( arr, n):
    n=len(arr)
    arr.sort()
    if (n%2) == 0:
        return arr[(n//2)-1]
    else:
        return arr[n//2]