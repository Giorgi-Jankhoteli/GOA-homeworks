def withdraw(m):
    sum = [0, 0, 0]
    while m > 0:
        if m - 100 >= 0 and m - 100 != 10 and m - 100 != 30:
            m = m-100
            sum[0] += 1
        elif m - 50 >= 0 and (m - 50) != 10 and (m - 50) != 30:
            m = m-50
            sum[1] += 1
        else:
            m = m-20
            sum[2] += 1
    return sum   