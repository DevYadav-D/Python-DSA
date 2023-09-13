def minAnd2ndMin( a, n):
    min = -1
    min2 = -1
    if n<2:
        return [min, min2]
    else:
        a.sort()
        min = a[0]
        for i in range(n-1):
            if a[i+1] != a[i]:
                min2 = a[i+1]
                return [min, min2]
        return [-1]