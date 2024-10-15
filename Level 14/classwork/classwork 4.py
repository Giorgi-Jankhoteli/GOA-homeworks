num1 = int(input("შემოიტანე რიცხვი: "))

num2 = 0

for i in range (1, num1):
    num2 = num2 + i

print(num2 // num1)