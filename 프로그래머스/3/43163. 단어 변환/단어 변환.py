from collections import deque

def oneword(a, b):
    diff = 0
    for i in range(0, len(a)):
        if diff > 1:
            return False
        if a[i] != b[i]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False

    
def solution(begin, target, words):
    
    n = len(words)
    count = 0
        
    starts = []
    targetIdx = -1
    for i in range(0, n):
        if oneword(begin, words[i]):
            starts.append(i)
        if words[i] == target:
            targetIdx = i
    if targetIdx == -1:
        return 0

    path = []
    
    for s in starts:
        stack = deque()
        visited = [0 for _ in range(n)]
        
        stack.append(s)
        
        while stack:
            now = stack.pop()
            visited[now] = 1
            path.append(now)
            # print("path", path)
            print("now", now)
            print("visited", visited)
            
            # if words[now] == target:
            count += 1
            if target == words[now]:
                return count
                

            for i in range(0, n):
                if visited[i] == 0 and oneword(words[now], words[i]) and i not in stack:
                    stack.append(i)
                    print("stack", stack)
            else:
                path
                        
                        
    print(path)
    answer = 0
    return count