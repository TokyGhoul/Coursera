'''
За день машина проезжает N километров.
Сколько дней нужно, чтобы проехать маршут длиной M километров?
'''
num1 = int(input())
num2 = int(input())

print((num2 - 1) // num1 + 1)
