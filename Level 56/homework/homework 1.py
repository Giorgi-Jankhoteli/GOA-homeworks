def nickname_generator(name):
    vowel = "aeiou"
    
    if len(name) < 4:
        return "Error: Name too short"
    
    if name[2].lower() in vowel:
        return name[:4]
    else:
        return name[:3]