def digitize(n):
    num = []
    str_n = str(n)
    for element in range(1,len(str_n)+1):
        num.append(int(str_n[-element]))
        
    return num