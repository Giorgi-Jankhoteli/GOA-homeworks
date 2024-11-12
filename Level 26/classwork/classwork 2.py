list1 = ["giorgi", "gabrieli", "dato", "nika", "saba"]
list2 = ["beqa", "zaza", "avto", "tazo", "luka"]

print(list1.index("giorgi"))

list1.insert(4, "zuka")
print(list1)

list1.extend(list2)
print(list1)

print(list1.count("giorgi"))