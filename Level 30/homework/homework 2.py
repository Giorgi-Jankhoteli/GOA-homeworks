list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 0

def plus(num, list):
    for i in range(len(list)):
        num += list[i]

    return num
    
print(plus(num, list))