
def simple_numbers(n):
    a = []
    for i in range(2,n):
        a.append(True)
    i = 2
    while i*i <= n:
        j = i*i
        if a[i] == True:
            while j <= n:
                a[j] = a.append(False)
                j += i
        i += 1
    for i in range(2,n):
        if a[i] == True:
            print(i)
b = int(input())
simple_numbers(b)
