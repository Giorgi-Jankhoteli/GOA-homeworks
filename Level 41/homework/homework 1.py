def filter_list(l):
    final_list = []
    for element in l:
        if type(element) == int:
            final_list.append(element)
    return final_list       