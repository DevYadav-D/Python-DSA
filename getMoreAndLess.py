def getMoreAndLess(arr, n, x):
        output =[0, 0]
        greater=0
        equal=0
        less=0
        for i in range(n):
            if arr[i]==x:
                equal +=1
            elif arr[i]>x:
                greater +=1
            else:
                less+=1
        output[0] = equal+less
        output[1] = equal+greater
        return output

