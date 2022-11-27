'''
(!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат. (0,0,0), (0,0,1) и тд.
'''

for x in range(2):
    for y in range(2):
        for z in range(2):
            LogicalExpression = not (x or y or z) == ((not x) and (not y) and (not z))
            if LogicalExpression:
                print(f'При x = {x}, y = {y} и z = {z} выражение истинно')
            else:
                print(f'При x = {x}, y = {y} и z = {z} выражение ложно')