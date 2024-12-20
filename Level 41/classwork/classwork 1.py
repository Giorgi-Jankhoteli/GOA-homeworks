def get_count(sentence):
    num = 0
    for element in sentence:
        if element == 'a' or element == 'e' or element == 'i' or element == 'o' or element == 'u':
            num += 1
    return num