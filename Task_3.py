'''
Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

while True:
    x = int(input('Введите абсциссу точки: '))
    y = int(input('Введите ординату точки: '))
    if x > 0 and y > 0:
        print('Точка принадлежит первой четверти')
    elif x < 0 and y > 0:
        print('Точка принадлежит второй четверти')
    elif x < 0 and y < 0:
        print('Точка принадлежит третьей четверти')
    elif x > 0 and y < 0:
        print('Точка принадлежит четвертой четверти')
    else:
        print('Это начало координат или какая-то полуплоскость')