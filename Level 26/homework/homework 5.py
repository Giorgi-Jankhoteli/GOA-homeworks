list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]
list4 = [13, 14, 15, 16]
list5 = [17, 18, 19, 20]

list1.extend(list2)
print(list1)

list1.extend(list3)
print(list1)

list5.extend(list4)
print(list5)

list4.extend(list3)
print(list4)

list5.extend(list1)
print(list5)