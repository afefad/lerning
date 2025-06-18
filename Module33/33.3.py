import test_import as my

# my.re.findall()
# my.random.randint()

text = 'AV is largest Analytics community of India.'

pattern = my.re.compile(r'\b[aeiouAEIOU]\w+')
result = pattern.findall(text)
print(result)

deep_ocean = """oCeAn Marlin 0cEaN oceAN OCEAN oCEAN OCEAN OCEAn OCEan OCean Ocean ocean oCeAn OcEaN oceAN ocEAN
                OCEAN OCEAn OCEan OCean Ocean ocean oCeAn OcEaN oceAN ocEAN oCEAN OCEAN OCEAn OCEan OCean Ocean
                ocean oCeAn OcEaN nemaa ocEAN oCEAN OCEAN OCEAn OCEan OCean nemo0 ocean oCeAn OcEaN oceAN ocEAN
                OCEAN OCEAN OCEAn OCEan OCean Ocean ocean oNeMa OcEaN oceAN ocEAN oCEAN OCEAN OCEAn OCEan OCean
                Ocean ocean oCeAn OcEaN oceAN nenemo OCEAN OCEAN OCEAn OCEan OCean Ocean Nemo ocean oCeAn OcEaN
                oceAN ocEAN oCEAN OCEAN OCEAn OCEan OCean Ocean ocean oCeAn OcEaN oceAN ocEAN oCEAN OCEAN OCEAn
                OCEan OCean Ocean ocean """

nemo_pattern = my.re.compile(r'[Nn]em\w{0,2}')

full_search = nemo_pattern.findall(deep_ocean)
print(full_search)

nemo_matched = my.re.search('Nemo', deep_ocean)
print(nemo_matched)

transperent = my.re.sub(r'[Oo]\w{4}\s+', '', deep_ocean)
print(transperent)

# # Практика
# Задача 1. Согласные
# Дан следующий текст:
# Even if they are djinns, I will get djinns that can outdjinn them.
#
# Используя регулярные выражения, напишите программу, которая выводит два списка:
#  - Первый содержит все слова, которые начинаются на гласную букву латинского алфавита
#     (в этот раз слово может состоять и из одной буквы, например I).
#  - Второй содержит слова, которые начинаются на любой символ,
#     кроме гласных букв латинского алфавита.
#
# Для получения второго списка за основу используйте шаблон, которым вы получили первый список.
#
# Ещё небольшая подсказка: посмотрите, чем отличается символ * от символа +.
# Также, когда будете получать второй список, обратите внимание, на какой символ начинаются слова.

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

result: my.List[str] = list(my.re.findall(r'\b[AaEeIiOoUu]\w+', text))
print(result)
result2: my.List[str] = list(my.re.findall(r'\b[^AaEeIiOoUu\s]\w+', text))
print(result2)

# Задача 2. Даты
# Из одного дата-центра пришёл текстовый пакет данных, который содержит информацию о кодовом названии оборудования,
# его серийном номере и дате начала эксплуатации. Вот небольшой кусочек из этого пакета в виде строки:
#
# Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009
#
# Используя регулярные выражения, напишите программу, получающую список всех дат, которые встречаются в строке.
# Для этого необходимо использовать \d.
# Ожидаемый результат:
#
# ['12-05-2007', '11-11-2011', '12-01-2009']

text2 = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
result3: my.List[str] = list(my.re.findall(r'\d{2}-\d{2}-\d{4}', text2))
print(result3)
