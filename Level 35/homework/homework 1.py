def count_sheeps(sheep):
    count = 0
    for element in sheep:
        if element == True:
            count += 1
    return count