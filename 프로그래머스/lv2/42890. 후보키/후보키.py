from itertools import combinations

def solution(relation):
    answer = 0
    candidates = []
    for i in range(1, len(relation[0])+1):
        for comb in combinations(list(range(len(relation[0]))), i):
            flag2 = 1
            for cand in candidates:
                if set(comb) > cand:
                    flag2 = 0
                    break
            if flag2:
                overlap = list()
                flag = 1
                for row in relation:
                    data = list()
                    for c in comb:
                        data.append(row[c])
                    if data in overlap:
                        flag = 0
                        break
                    else:
                        overlap.append(data)
                    print(overlap)
                if flag:
                    candidates.append(set(comb))
                    answer += 1
    
    return answer