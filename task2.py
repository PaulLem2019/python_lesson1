"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

sec = int (input ("Введите время в секундах "))

hour = sec // 3600
minutes = (sec % 3600) // 60
second = sec % 3600 % 60

print (f'{hour}:{minutes}:{second}')
