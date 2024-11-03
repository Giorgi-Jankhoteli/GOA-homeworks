num1 = [10, 2, 30, 4, 5, 60, 7, 8, 90, 10]
num2 = []

for num1 in num1:
    if int(num1) < 10:
        num2.append(num1)

print(num2)