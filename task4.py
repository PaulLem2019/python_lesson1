"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int (input ("Введите целое положительное число "))

beg_number = number
maximal = number % 10

while number > 0:
    if (number % 10) > maximal:
        maximal = number % 10

    number //= 10

print (f'{maximal} - максимальное цифра в числе {beg_number}')

