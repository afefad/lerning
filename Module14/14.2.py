def numeral_count(number):
    if number < 0:
        print('Число отрицательное, обнуляю!')
        return 0

    count = 0
    while number > 0:
        number //= 10
        count += 1

    return count


firstTask, secondTask = int(input()), int(input())

firstNumeral = numeral_count(firstTask)
secondNumeral = numeral_count(secondTask)


if firstNumeral > secondNumeral:
    print('Цифр больше в первом числе')
elif firstNumeral < secondNumeral:
    print('Цифр больше во втором числе')
else:
    print('Равное количество цифр')
