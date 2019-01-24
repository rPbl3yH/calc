from random import randint
k = ['Манчестер Юнайтед','Ювентус','Арсенал','Турин','Реал Мадрид',
'РОССИЯ','Зенит','ЦСКА Москва','Боруссия Д','Наполи','Милан','Бавария',
'Манчестер Сити','Локомотив Москва','Интер Милан','Анжи','Барселона','ПСЖ','Рома ','Атлетико М ']   #Команды
n = 20                                                                                                  #Количество команд
sc=[randint(1,100) for i in range(n)]
                                                                                             
for i in range(n):
    print(k[i],'score: ',sc[i],sep = ' ')                                                           #Выводим список команд
print()
for i in range(n-1):
    for j in range(n-i-1):
        if sc[j] < sc[j+1]:
            sc[j],sc[j+1] = sc[j+1],sc[j]
            k[j],k[j+1] = k[j+1],k[j]
print()
for i in range(n):
    print(k[i],'score: ',sc[i],sep = ' ')
print('')
v = input()
i = 0
for sl in k:
    if sl == v:
        print(k[i],'score: ',sc[i],sep = ' ')
    i += 1

