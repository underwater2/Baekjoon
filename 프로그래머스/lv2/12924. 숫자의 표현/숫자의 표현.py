def solution(n):
    answer = 0
    for i in range(1, n//2+1):
        flag = 1
        s = i
        j = i
        while flag:
            j += 1
            s += j
            if s == n:
                answer += 1
                break
            elif s > n:
                break
    return answer+1