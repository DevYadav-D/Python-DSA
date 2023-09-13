def scores(self, a, b, cc):
    # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
    for i in range(len(a)):
        if a[i]==b[i]:
            continue
        elif a[i]>b[i]:
            cc[0] += 1
        else:
            cc[1] +=1
    return cc