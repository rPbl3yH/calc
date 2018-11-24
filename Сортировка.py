
def sort(n):
    n=n.split()
    s=len(n)
    for i in range(0,s-1):
        for j in range(0,s-i-1):
            if n[j+1]<n[j]:
                k=n[j]
                n[j]=n[j+1]
                n[j+1]=k
    for i in range(s):
        print(n[i])
    return n,s,k
k=input()
sort(k)
