def basic_op(operator, value1, value2):
    #your code here
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return " "
    
    print(basic_op("+", 4, 7))
    print(basic_op('-', 15, 18))
    print(basic_op("*", 5, 5))
    print(basic_op("/", 49, 7))