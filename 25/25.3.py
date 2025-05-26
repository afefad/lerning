def divide(number):
    return 10 / number

def sum_of_devided(left, right):
    div_sum = 0
    for i_num in range(left, right + 1):
        try:
            div_sum += divide(i_num)
            print(div_sum)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
    return div_sum

total = 0
try:
    numbers_file = open('numbers.txt', 'r')
    for i_line in numbers_file:
        num_list = i_line.split()
        first_num = int(num_list[0])
        second_num = int(num_list[1])

        total += sum_of_devided(first_num, second_num)
    print(f'Общая сумма: {total}')

except ZeroDivisionError:
    print('На ноль делить нельзя!')

answer_file = open('answer.txt', 'w', encoding='utf8')
try:
    answer_file.write(int('Ответ: '))
    answer_file.write(total)
except TypeError:
    print('Ошибка записи в файл, тип данных не строка')
else:
    print('Программа выполнилась без ошибок!')
finally:
    answer_file.close()
    print('Файл answer.txt закрыт.' if answer_file.closed else 'Файл answer.txt не закрылся!')