from enum import unique

phone_nums = [
    '+380501234568',
    '+380501234568',
    '+380501234568',
    '+380501234568',
    '+380501234569',
    '+380501234570',
    '+380501234570',
    '+380501234567',
    '+380501234567',
    '+380501234567',
    '+380501234571'
]

unique_list = []
for i in range(len(phone_nums)):
    print('текущий индекс =', i)
    if i != len(phone_nums)-2 and phone_nums[i] != phone_nums[i+1]:
        unique_list.append(phone_nums[i])
    elif i == len(phone_nums)-2 and phone_nums[i] != phone_nums[i+1]:
        unique_list.append(phone_nums[i])
        unique_list.append(phone_nums[i+1])
    elif i == len(phone_nums):
        continue

print(unique_list)