answer = -1

def solution(exp):
    calc(exp, '*', '+', '-')
    calc(exp, '*', '-', '+')
    calc(exp, '+', '*', '-')
    calc(exp, '+', '-', '*')
    calc(exp, '-', '*', '+')
    calc(exp, '-', '+', '*')
    return answer

def calc(exp, e1, e2, e3):
    global answer
    exp = exp.split(e3)
    for i in range(len(exp)):
        newexp = exp[i].split(e2)
        for j in range(len(newexp)):
            newexp[j] = str(eval(newexp[j]))
        exp[i] = str(eval(e2.join(newexp)))
    if abs(eval(e3.join(exp))) > answer:
        answer = abs(eval(e3.join(exp)))
