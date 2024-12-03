def no_space(x):
    #your code here
    strr = ""
    for char in x:
        if char != " ":
            strr += char
    return strr