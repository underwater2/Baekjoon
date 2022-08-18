from collections import Counter

def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    for p in part:
        try:
            if part[p] == comp[p]:
                continue
            else:
                return p
        except:
            return p
    answer = ''
    return answer