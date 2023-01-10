#!/usr/bin/python3

print('Привет, для выбора системы исчисления впишите цифру Где: ')
print('ДВОИЧНАЯ:"2"')
print('ТРОИЧНАЯ:"3"')
print('ЧЕТВЕРИЧНАЯ:"4"')
print('ПЯТЕРИЧНАЯ:"5"')
print('ШЕСТЕРИЧНАЯ:"6"')
print('СЕМЕРИЧНАЯ:"7"')
print('ВОСМЕРИЧНАЯ:"8"')
print('ДЕВЯТЕРИЧНАЯ:"9"')
print('ДЕСЯТЕРИЧНАЯ:"10"')

iz = int(input('Выберите систему исчисления ИЗ какой переводим: '))   #Вибираем из какой переводим
vk = int(input("Выберите систему исчисления В какую переводим: "))    #Выбираем в какую переводим
ch = int(input("Впишите число: "))

#Рабочие переменные 

stepen = 0
vivod = 0
spisok2 = []
vivod2 = ''

#Из любой в 10

spisok=list(str(ch))
spisok.reverse()

for i in spisok:
    vivod += (int(i)*iz**stepen)
    stepen = stepen + 1

if vk == 10:
    print('Результат:',vivod)

#Из 10 в любую

if not vk == 10:
    while vivod >= 1:
        spisok2.append(vivod % vk)
        vivod = vivod//vk

spisok2.reverse()

for r in spisok2:
    vivod2 += str(r)
    
if not vk == 10:
    print("Результат:",vivod2)
    
