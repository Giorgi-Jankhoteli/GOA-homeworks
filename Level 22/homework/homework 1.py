list1 = ["Giorgi", "Gabrieli", "Vano", "Nika", "Beqa", "Aleqsandre", "Mate", "Irakli", "Saba", "Shotiko", "Sandro", "Luka"]
list2 = []

for list1 in list1:
    if len(list1) > 4:
        list2.append(list1)
print(list2)