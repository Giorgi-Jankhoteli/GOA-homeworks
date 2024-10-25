num = int(input("შეიყვანეთ რიცხვი 1 დან 7 მდე: "))

for i in range(1):
    if num == 1:
        print("ორშაბათი")
    elif num == 2:
        print("სამშაბათი")
    elif num == 3:
        print("ოთხშაბათი")
    elif num == 4:
        print("ხუთშაბათი")
    elif num == 5:
        print("პარასკევი")
    elif num == 6:
        print("შაბათი")
    elif num == 7:
        print("კვირა")
    else:
        print("არ არსებობს კვირის დღე")