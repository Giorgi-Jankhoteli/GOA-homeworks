def poss_or_neg(a):
    if a > 0:
        return "Possitive"
    elif a < 0:
        return "Negative"
    else:
        return "Equals 0"
    
print(poss_or_neg(0))