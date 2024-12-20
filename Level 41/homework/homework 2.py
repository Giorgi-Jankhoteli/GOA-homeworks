def to_jaden_case(string):
    my_list=[]
    word = string.split()
    for x in word:
        my_list.append(x.capitalize())
    string = ' '.join(my_list)
    return string