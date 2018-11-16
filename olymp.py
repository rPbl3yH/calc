n=int(input('Enter your number '))
k=9
l=[]
if (n%2==0)or(n%3==0)or(n%5==0)or(n%7==0):
    while n>1:
        #print(k)
        #print(n)
        if n%k==0:
            n=n//k
            l.append(str(k))
            #print(n)
            if n%2==1 and n%3!=1 and n%5!=1 and n%7!=0:
                l.clear()
                print(-1)
                break
            k=9
        k=k-1
    l.sort()
    print(''.join(l))
    #print(l)
else: print(-1)
        
