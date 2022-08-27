from collections import deque

def solution(prices):
    stack = deque()
    answer = [0] * len(prices)
    # 가격이 내려갔을 때
    for i in range(len(prices)):
        if stack and prices[i] < stack[-1][1]:
            while stack and stack[-1][1] > prices[i]:
                temp = stack.pop()
                answer[temp[0]] = i-temp[0]
        stack.append((i, prices[i]))
    if stack:
        for s in stack:
            answer[s[0]] = len(prices)-1-s[0]
    return answer