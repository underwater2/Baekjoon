from collections import deque

di = [0, 1, 0, -1]  # 우하좌상
dj = [1, 0, -1, 0]

def solution(maps):
    n, m = len(maps[0]), len(maps)
    queue = deque([(0,0,1)])
    maps[0][0] = 1
    while queue:
        i, j, cnt = queue.popleft()
        for t in range(4):
            ni = i+di[t]
            nj = j+dj[t]
            if 0 <= ni < m and 0 <= nj < n and maps[ni][nj]:
                if (ni, nj) == (m-1, n-1):
                    return cnt+1
                maps[ni][nj] = 0
                queue.append((ni, nj, cnt+1))
    return -1