'''
Электронные часы показывают время в формате h:mm:ss, то есть сначала
записывается количество часов (число от 0 до , потом обязательно двузначное
количество минут, затем обязательно двузначное количество секунд.
Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

С начала суток прошло N секунд. Выведите, что покажут часы.
'''
num = int(input())

print(str(num // 3600 % 24) + ':', end='')
print(str(num % 3600 // 60 // 10) + str(num % 3600 // 60 % 10) + ":", end='')
print(str(num % 60 // 10) + str(num % 60 % 10))
