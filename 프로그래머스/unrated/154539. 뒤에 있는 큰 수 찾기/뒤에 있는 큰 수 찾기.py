from collections import deque

def solution(numbers):
    stack = deque()
    answer = [0] * len(numbers)
    for i in range(len(numbers)-1, -1, -1):
        if not stack:
            stack.append(numbers[i])
            answer[i] = -1
        else:
            while stack and stack[-1] <= numbers[i]:
                stack.pop()
            if stack:  
                answer[i] = stack[-1]
                stack.append(numbers[i])
            else:
                answer[i] = -1
                stack.append(numbers[i])
    return answer