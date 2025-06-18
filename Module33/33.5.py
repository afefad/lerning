import itertools

colors = ['красный', 'синий', 'зелёный', 'жёлтый']

for i in itertools.permutations(colors, 3):
    print(i)

print('\n' + '=' * 40 + '\n')

for i in itertools.combinations(colors, 2):
    print(i)

my_cycle = itertools.cycle(['one', 'two', 'three'])
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))
print(next(my_cycle))