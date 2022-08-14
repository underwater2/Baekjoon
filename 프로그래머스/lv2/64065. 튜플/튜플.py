import re

def solution(s):
    p = re.compile('[{},]+')
    nums = p.split(s)[1:-1]
    hashli = dict()
    for num in nums:
        if num in hashli:
            hashli[num] += 1
        else:
            hashli[num] = 1
    sortli = sorted(hashli.items(), key=lambda x: -x[1])
    answer = []
    for tup in sortli:
        answer.append(int(tup[0]))
    return answer