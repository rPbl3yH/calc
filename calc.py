def fact(n):
    f = 1
    for i in range(1,n+1):
            f *= i
    print('Результат:',f)
    print()
    return n,f
from random import randint as privet
from math import *
pr1=str('Дороу,братишь,как жизнь?Как звать то?')
pr2=str('Как тебя зовут?')
pr3=str('Хей,ла,ла,лей.Зовут как? Ха,и так знаю,что ла,ла,лей)')
pr4=str('Ваше имя, Господин')
pr=[pr1,pr2,pr3,pr4]
print(pr[privet(0,3)])
p=input('Введите свое имя ')
print('OK,',p,'! А меня ИЛОН 1000. Будем знакомы!')
print('Если я буду тебе надоедать, то ты можешь выключить меня, нажав "#"')
print('Во мне есть несколько функций:')
while 1==1: 
    print('Введите "+", чтобы провести сложение')
    print('Введите "-", чтобы провести вычитание')
    print('Введите "*", чтобы провести умножение')
    print('Введите "/", чтобы провести деление')
    print('Введите "fact", чтобы провести факториал')
    print('Введите "sqrt", чтобы провести деление')
    n = input('Выбор операции: ')
    if n == '+':
        a=int(input('Введите первое слагаемое: '))
        b=int(input('Введите второе слагаемое: '))
        print('Результат:',a+b)
        print()
    elif n == '-':
        a=int(input('Введите уменьшаемое: '))
        b=int(input('Введите вычитаемое: '))
        print('Результат:',a-b)
        print()
    elif n == '*':
        a=int(input('Введите первый множитель: '))
        b=int(input('Введите второй множитель: '))
        print('Результат:',a*b)
        print()
    elif n == '/':
        a=int(input('Введите делимое: '))
        b=int(input('Введите делитель: '))
        print('Результат:',a/b)
        print()
    elif n == 'fact':
        a = int(input('Введите число: '))
        fact(a)
    elif n == 'sqrt':
        a = int(input('Введите число: '))
        a = int(sqrt(a))
        print('Результат: ',a)
    elif n =='#':
        break
    else: print()

        
