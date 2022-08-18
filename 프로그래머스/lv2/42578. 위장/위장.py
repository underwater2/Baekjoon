from collections import defaultdict

def solution(clothes):
    answer = 1
    dt = defaultdict(list)
    for c in clothes:
        dt[c[1]].append(c[0])
    for d in dt:
        answer *= (len(dt[d])+1)
    return answer-1