def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    idx = 0
    while idx < len(citations):
        if citations[idx] >= idx+1:
            answer = idx+1
            idx += 1
        else:
            break
    return answer