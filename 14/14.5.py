from math import e, factorial

# Задаётся точность в формате 0.0...1
precision = float(input('Точность: '))

result = 0
i = 0
addMember = 1
while addMember > precision:
    addMember = 1 / factorial(i)
    result += addMember
    i += 1

print('Результат:', result)
print('Константа:', e)
