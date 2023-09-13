def streamAvg(arr, n):
    sum = 0
    avg = []
    for i in range(n):
        sum += arr[i]
        avg.append(sum/(i+1))
    return avg