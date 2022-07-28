#3 - Задайте список из n чисел последовательности
#  (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 
# 4: 2.44140625, 5: 2.4883199999999994,
#  6: 2.5216263717421135}

def digit_check():
    try:
        n = int(input('Введите число n: '))
        return n
    except ValueError:
        print('Пожалуйста, введите число!')
        return digit_check()
n = digit_check()
dict = {}
for i in range(1, 1+n):
    dict[i] = dict.get(i, (1+1/i)**i)
print(dict)
sum1 = sum(dict[i] for i in dict)
print("Сумма значений ключей:", sum1)
print("Сумма ключей:", sum(dict))
