def is_valid_walk(walk):
    n = walk.count("n")
    s = walk.count("s")
    w = walk.count("w")
    e = walk.count("e")
    
    if len(walk) != 10:
        return False
    if n == s and w == e:
        return True
    else:
        return False