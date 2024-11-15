num = int(input("შემოიტანე რიცხვი: "))

if num % 2 == 0:
    print(num // 2)
elif num % 2 != 0:
    print(num * 3 + 1)