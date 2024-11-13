list1 = [1, 2, 4, 5, 66, 1000, 22, 20, 11, 13, 24, 30, 65, 77, 89]
list2 = []

for index in list1:
    if index % 2 != 0:
        list2.append(index)
print(list2)