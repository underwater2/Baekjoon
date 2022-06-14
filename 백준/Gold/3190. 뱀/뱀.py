import sys

from collections import deque

dx = [0, 1, 0, -1] #우하좌상
dy = [1, 0, -1, 0]
D = 0

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

apple = []
for _ in range(K):
    ai, aj = map(int, sys.stdin.readline().split())
    apple.append((ai-1, aj-1))

L = int(sys.stdin.readline())
direction = []
for _ in range(L):
    di, dj = sys.stdin.readline().split()
    direction.append((int(di), dj))

S = 0 # S초 끝
i, j = 0, 0
snake = deque([(0, 0)])
while True:
    S += 1
    i += dx[D]
    j += dy[D]

    if i < 0 or i > N-1 or j < 0 or j > N-1 or (i, j) in snake:
        break

    if (i, j) in apple: # 옮겨간 곳에 사과가 있으면
        apple.remove((i, j))
    else:
        snake.pop()
    snake.appendleft((i, j))

    for dirc in direction:
        if dirc[0] == S:
            if dirc[1] == 'D':
                D += 1
                if D > 3:
                    D = D % 4
            else: # 'L'
                D -= 1
                if D == -1:
                    D = 3

print(S)