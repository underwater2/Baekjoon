def solution(string):
    flag = 0
    for s in string:
        if s == '(':
            flag += 1
        else:
            flag -= 1
        if flag < 0:
            return False
    if flag != 0:
        return False
    return True