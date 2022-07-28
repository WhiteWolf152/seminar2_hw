#1 - Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
#*Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def digit_check():
    try:
        a = float(input('Введите число: '))
        return a
    except ValueError:
        print('Пожалуйста, введите число!')
        return digit_check()
a = digit_check()
str_a = str(a)
str_a = str_a.replace('.', '')
lst_str = list(str_a)
lst_num = map(int, lst_str)
Sum = sum(lst_num)
print(Sum)