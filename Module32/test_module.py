def func() -> None:
    print('Я функция func() из модуля test_module.py')

if __name__ == '__main__':
    print('Здесь какой то основной код')
    func()
else:
    print(f'Импортирован модуль {__name__}')