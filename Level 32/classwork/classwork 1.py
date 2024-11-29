def remove_char(s):
    new_word = []
    empty = ""

    for i in s:
        new_word.append(i)
    new_word.pop(0)
    new_word.pop(-1)

    for i in new_word:
        empty += i
        
    return empty