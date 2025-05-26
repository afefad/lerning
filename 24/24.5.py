speakers_file = open('speakers.txt', 'r', encoding='utf8')
data = speakers_file.read(14)
speakers_file.seek(26)
data2 = speakers_file.read(18)
print(data)
print(data2)
speakers_file.close()


