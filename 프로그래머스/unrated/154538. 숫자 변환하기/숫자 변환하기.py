from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    # bfs
    queue = deque()
    queue.append((x, 0))
    
    visited = [0] * (y+1)
    while queue:
        num, cnt = queue.popleft()
        if y in [num+n, num*2, num*3]:
            return cnt+1
        if num+n < y and not visited[num+n]:
            queue.append((num+n, cnt+1))
            visited[num+n] = 1
        if num*2 < y and not visited[num*2]:
            queue.append((num*2, cnt+1))
            visited[num*2] = 1
        if num*3 < y and not visited[num*3]:
            queue.append((num*3, cnt+1))
            visited[num*3] = 1
    return -1