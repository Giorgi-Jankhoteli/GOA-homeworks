age = int(input("Your age: "))

for _ in range(1):
    if age > 18:
        print("You are adult")
    elif age < 18:
        print("You are virgin")