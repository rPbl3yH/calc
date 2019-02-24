n = int(input())
k = int(input())
x = int(input())
znach_a = x//(n-k)
znach_a_1 = x//(n-k)+1
if x % (n-k) == 0:
    print(n*znach_a)
else:
    print(x + k*(znach_a+1))
print(znach_a)
print(znach_a_1)
