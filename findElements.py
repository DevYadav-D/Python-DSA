def findElements(a, n):
    a.sort()
    if n>=3:
        a = a[:n-2]
        return a
    else:
        return a 