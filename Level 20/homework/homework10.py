num = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

count1 = 0
count2 = 0

for num in num:
    if num > 0:
        count1 += 1
    elif num < 0:
        count2 += 1
    
print(count1)
print(count2)