test = 1

#Error
def f1():
    print(test)
    test = 7
    print(test)

# f1()
print('\n')

def f2():
    test = 2
    print(test)

    if 'test' not in globals():
        print('not in globals')
        raise Exception
    if 'test' not in locals():
        print('not in locals')
        raise Exception

# f2()
print('\n')

def func():
    var = 1

    # Error
    def f3():
        par = 2
        if 'var' not in locals():
            raise Exception
        print('var' in locals())

    # f3()

    def f4():
        par = 3
        print(var)
        if 'var' not in locals():
            raise Exception

    # f4()

    def f5():
        var = 4
        par = 4
        print(var)
        if 'var' not in globals():
            raise Exception

    # Error
    f5()

func()
print('\n')