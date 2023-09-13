def lastIndex(s):
    s=list(s)
    s=s[::-1]
    for i in range(len(s)):
        if s[i]=='1':
            return len(s)-(i+1)
    return -1