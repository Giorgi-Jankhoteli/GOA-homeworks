num1 = [1, 4, 3, 6, 5, 8, 9, 10, 20, 17, 18, 22, 60, 100]
num2 = []

for item in num1:
    if item % 2 == 0:
        num2.append(item)
    
print(num2)