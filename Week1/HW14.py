'''
Дано целое число N. Выведите следующее за ним четное число.
'''
num = int(input())

if num % 2 == 0:
    print(num + 2)
else:
    print(num + 1)
