# Задача 1

buckwheat_bag = 100
buckwheat_per_month = 4
mounth = 0

print('Информация о запасах гречки:')

for _ in range(buckwheat_per_month, buckwheat_bag + 1, buckwheat_per_month):
    mounth += 1
    print('Через', mounth, 'месяц:', buckwheat_bag - mounth * buckwheat_per_month, 'кг гречки в запасе')

print()
print('Запасы гречки закончились.')


# Задача 2

debtors = int(input('Введите количество должников: '))
step = 5
debt = 0

for current_debtor in range(0, debtors, step):
    print('Должник с номером', current_debtor)
    debt += int(input('Сколько должны? '))

print('Общая сумма долга:', debt)


# Задача 3

reverse_timer = int(
    input('Введите время для обратного отсчёта (в секундах): '))
print('Таймер установлен на', reverse_timer, 'секунд.')

for time in range(reverse_timer, 0, -1):
    print('Осталось:', time, 'секунд')
    option = int(
        input('Введите 1, если еда готова, или 0, чтобы продолжить: '))
    if option == 1:
        print('Ваша еда готова, можете забрать! Таймер был прерван на', time, 'секундах.')
        break
    elif option != 0:
        print('Неверный ввод.')
        break
else:
    print('Ваша еда готова. Осторожно, горячo!')


# Задача 4

start_of_line = int(input('Введите начало отрезка: '))
end_of_line = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))

while end_of_line == start_of_line:
    print('Некорректная длина отрезка. начало отрезка и конец отрезка не могут быть одинаковыми.')
    start_of_line = int(input('Введите начало отрезка: '))
    end_of_line = int(input('Введите конец отрезка: '))

while step == 0:
    step = int(input('Шаг не может быть нулевым. Введите коорректный шаг: '))

if end_of_line < start_of_line:
    end_of_line, start_of_line = start_of_line, end_of_line

step = -abs(step)

print('Значения функции на отрезке с шагом', step, ':')

for x in range(end_of_line, start_of_line - 1, step):
    y = x ** 3 + 2 * x ** 2 - 4 * x + 1
    print('В точке', x, 'значение функции равно', y)


# Задача 5

educational_grant = int(input('Введите ежемесячную стипендию: '))
living_expenses = int(input('Введите ежемесячные расходы: '))
indexation = 0.03
months_of_education = 10
money_needed = 0


for month in range(1, months_of_education + 1):
    expenses = living_expenses - educational_grant
    print(month, 'месяц: траты', living_expenses, 'рублей, не хватает', expenses ,'рублей.')
    living_expenses = int(living_expenses * (1 + indexation))
    money_needed += expenses

print('Сумма денег, которую необходимо получить у родителей:', money_needed, 'рублей.')
