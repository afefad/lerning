import time

phone_nums = ['+380501234567', '+380501234568', '+380501234569', '+380501234570', '+380501234567', '+380501234571']

curr_time = time.time()
unic_nums = set(phone_nums)
print(type(unic_nums), ':', unic_nums)
end_time = time.time()
print('Время выполнения первого способа:', end_time - curr_time)

curr_time = time.time()
unic_nums: list = []
for i in phone_nums:
    if i not in unic_nums:
        unic_nums.append(i)
print(type(unic_nums), ':', unic_nums)
end_time = time.time()
print('Время выполнения первого способа:', end_time - curr_time)

