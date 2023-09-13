def palinArray(arr,n):
    for i in range(n):
        s = str(arr[i])
        if (s[::-1] == s):
            continue
        else:
            return 0
    return 1