# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = int(input()) # вводим количество монеток
heads = input() # вводим их расположение (H - орел, T - решка)
heads_count = heads.count('H') # считаем количество монеток орлом
tails_count = n - heads_count # считаем количество монеток решкой
print(min(heads_count, tails_count)) # выводим минимальное количество монеток, которые нужно перевернуть
# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает 
# две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные 
# Петей числа.
s = int(input()) # вводим сумму чисел
p = int(input()) # вводим их произведение
for x in range(1, 1001): # перебираем все возможные значения X
    y = s - x # вычисляем Y по формуле S = X + Y
    if x * y == p: # проверяем, удовлетворяют ли числа условиям
        print(x, y) # если да, выводим их и завершаем программу
        break
# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input()) # вводим число N
k = 0 # начальное значение степени двойки
while 2 ** k <= n: # пока степень двойки не превысит N
    print(2 ** k) # выводим степень двойки
    k += 1 # увеличиваем значение степени на 1