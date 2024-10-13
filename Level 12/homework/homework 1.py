num1 = int(input("შემოიტანე პირველი რიცხვი: "))
num2 = int(input("შემოიტანე მეორე რიცხვი: "))
action = (input("შემოიტანეთ მათემატიკური მოქმედება: "))
if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
elif action == "**":
    print(num1 ** num2)
elif action == "/":
    print(num1 / num2)
elif action == "//":
    print(num1 // num2)
elif action == "%":
    print(num1 % num2)
else:
    print("ამოხსნა შეუძლებელია")