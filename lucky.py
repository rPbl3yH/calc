b=0
def bilet(k):
    a=0
    s=int(input('Введите первое число: '))
    s1=int(input('Введите второе число: '))
    for a in range(s-1,s1+1,1):
        count1=a//100000
        count2=a//10000
        count2=count2%10
        count3=a//1000
        count3=count3%10
        count4=a%1000
        count4=count4//100
        count5=a%100
        count5=count5//10
        count6=a%10
        if count1+count2+count3==count4+count5+count6:
            k=k+1
    print('Кол-во счастливых билетов:',k)
    return s,s1,k,a
bilet(b)
                            
            
