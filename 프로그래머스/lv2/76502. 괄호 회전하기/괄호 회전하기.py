from collections import deque

def solution(s):
    que = deque(list(s))
    que.rotate(1)
    stack = deque()
    answer = 0
    for _ in range(len(s)-1):
        stack.clear()
        que.rotate(-1)
        for q in que:
            if q in ('{', '[', '('):
                stack.append(q)
            else:
                try:
                    next = stack.pop()
                    if (q == '}' and next != '{') or (q == ']' and next != '[') or (q == ')' and next != '('):
                        break
                except:
                    break
        else:
            if stack:
                break
            else:
                answer += 1
    return answer