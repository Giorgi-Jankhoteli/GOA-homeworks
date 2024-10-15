num = int(input("შემოიტანე რიცხვი: ")) 

for _ in range(1):
    if num > 0:
        print("შენი რიცხვი დადებითია")
    elif num < 0:
        print("შენი რიცხვი უარყოფითია")
    else:
        print("შენი რიცხვი 0ის ტოლია")