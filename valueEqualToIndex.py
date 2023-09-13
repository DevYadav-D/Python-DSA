def valueEqualToIndex(arr,n):
    output = []
    if n>1:
        for i in range(n):
            if i+1 == arr[i]:
                output.append(i+1)
        if output is None:
            return 0
        else:
            return output
    else:
        None