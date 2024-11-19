num = [1, 3, 22, 4, 55, 10, 88, 100, 25, 5, 6, 77, 20, 65, 79, 49,]

print(max(num))

i = num[0]
for element in num:
    if element > i:
        i = element
print(i)