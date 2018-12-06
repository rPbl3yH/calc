def sortirovka(n):
    n=n.split()
    s=len(n)
    for i in range(s-1):
        for j in range(s-i-1):
            if int(n[j+1])<int(n[j]):
                l=n[j]
                n[j]=n[j+1]
                n[j+1]=l
    for i in range(s):
        print(n[i])
    return n,s,l
k=input()
sortirovka(k)
