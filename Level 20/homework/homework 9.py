list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = 0
odd = 0

for number in list:
    if number % 2 == 0:
        even += number
    else:
        odd += number

print(even)
print(odd)