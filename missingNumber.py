def missingNumber( A, N):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    return int((N*(N+1)/2))-sum  
