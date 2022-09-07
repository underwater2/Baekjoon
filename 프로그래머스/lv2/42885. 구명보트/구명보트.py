from collections import deque

def solution(people, limit):
    people.sort()
    que = deque(people)
    answer = 0
    while que:
        now = que.popleft()
        while que and que[-1] > limit-now:
            que.pop()
            answer += 1
        if que:
            que.pop()
        answer += 1
    return answer