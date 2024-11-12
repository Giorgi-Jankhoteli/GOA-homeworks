my_list = ["giorgi", "gabrieli", "daviti", "nika", "levani", "giorgi"]
# ------------------------------
# index

print(my_list.index("giorgi"))
# -------------------------------
# insert

my_list.insert(4, "zuka")
print(my_list)

my_list.insert(3, 12)
print(my_list)
# --------------------------------
# extend

num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]
num1.extend(num2)
print(num1)

num1.extend(num2)
num2.extend(num1)
print(num2)

num1.extend(["giorgi", 10])
print(num1)
# ---------------------------------
# count

print(my_list.count("giorgi"))
# ---------------------------------
# append
# remove
# pop
# insert
# extend
# index
# len
# count
# ---------------------------------
index = 0
for element in my_list:
    if element == "daviti":
        print(index)

    index += 1