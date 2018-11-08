a = [] 
n = int(input())  
for i in range(n):  
    num = int(input())
    a.append(num)
    a.sort()
for i in range(n):
    print(str(a[i]))
