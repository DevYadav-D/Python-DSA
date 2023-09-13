def findIndex (a, N, key ):
        output=[-1, -1]
        for i in range(N):
            if a[i]==key and output[0] == -1:
                output[0], output[1] = i,i
            elif a[i] == key and output[0] != -1:
                output[1] = i
        return output