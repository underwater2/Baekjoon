import sys
sys.setrecursionlimit(100000)

def left(r, c, d):
    if d == 0:
        c -= 1
    elif d == 1:
        r -= 1
    elif d == 2:
        c += 1
    else:
        r += 1
    return r, c

def back(r, c, d):
    if d == 0:
        r += 1
    elif d == 1:
        c -= 1
    elif d == 2:
        r -= 1
    else:
        c += 1
    return r, c

N, M = map(int, sys.stdin.readline().split())

r, c, d = map(int, sys.stdin.readline().split())

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate(r, c, d, cnt):
    lr, lc = left(r, c, d)
    if maps[lr][lc] == 0:
        d = (d + 3) % 4
        return cleaning(lr, lc, d)
    else:
        if cnt != 4:
            d = (d + 3) % 4
            return rotate(r, c, d, cnt+1)
        else:
            # 뒤쪽이 벽이면
            br, bc = back(r, c, d)
            if maps[br][bc] == 1:
                return
            else:
                return rotate(br, bc, d, 0)

# 1번
def cleaning(r, c, d):
    maps[r][c] = 2

    return rotate(r, c, d, 0)


cleaning(r, c, d)

ans = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            ans += 1
print(ans)