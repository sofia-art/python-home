"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
ex = {}
numbers = str(input())
n = len(list(numbers))
ex[numbers] = n
print (ex)