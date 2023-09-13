def convertFive(n):
    n=list(str(n))
    for i in range(len(n)):
        if n[i]=="0":
            n[i]="5"
    return int("".join(n))