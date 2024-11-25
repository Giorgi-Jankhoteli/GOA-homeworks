def solution(string):
    if string is None:
        return 'h'
    elif string == '':
        return ''
    else:
        return string[::-1]
    
print(solution('world'))
print(solution('word'))
print(solution('hello'))
print(solution(''))
print(solution(None))