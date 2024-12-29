def lowercase_count(strng):
    count = 0
    for element in strng:
        if element.islower():
            count += 1
        else:
            continue
    return count