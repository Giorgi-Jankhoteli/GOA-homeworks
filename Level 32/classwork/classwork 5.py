def positive_sum(arr):
    sum = 0
    for elements in arr:
        if elements > 0:
            sum += elements
    return sum