def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    
    num = (ppg / mpg) * 48
    return round(num, 1)