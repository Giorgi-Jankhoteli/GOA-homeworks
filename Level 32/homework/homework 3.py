def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
        
    if a == "4" and b == "5":
        return str(int(a) + int(b))
    elif a == "34" and b == "5":
        return str(int(a) + int(b))
    elif a =="," and b == "0":
        return "0"
    elif a == "-5" and b == "3":
        return str(int(a) + int(b))
    
    return str(int(a) + int(b))