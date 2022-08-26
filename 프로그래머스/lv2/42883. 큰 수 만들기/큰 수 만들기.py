from collections import deque

def solution(number, k):
    stack = deque()
    cnt = 0
    for num in number:
        while stack and stack[-1] < num and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(num)
    if cnt != k:
        return ''.join(stack)[:-(k-cnt)]
    return ''.join(stack)
        
    