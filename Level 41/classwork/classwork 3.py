def high_and_low(numbers):
    my_list = numbers.split()
    high = int(my_list[0])
    low = int(my_list[0])
    
    for element in my_list:
        if int(element) > high:
            high = int(element)
            
    for element in my_list:
        if int(element) < low:
            low = int(element)
            
    return str(high) + " " + str(low)