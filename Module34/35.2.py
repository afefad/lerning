from typing import List, Tuple
my_list: List = [10, 6, 15, 93, 42, 7, 32]
ages = my_list.sort()

def maxAge(data: list|tuple|List|Tuple):
    intList = []

    def maxTemp(data):
        maxInt = None

        for i in data:
            if maxInt == None or i > maxInt:
                maxInt = i
        return maxInt

    for _ in range(3):
        intList.append(maxTemp(data))
        data.remove(maxTemp(data))

    return intList

print(maxAge(my_list))
