import sys

def w(a, b, c):

    if wN[a][b][c]:
        return wN[a][b][c]

    elif a > 70 or b > 70 or c > 70:
        if wN[70][70][70]:
            return wN[70][70][70]
        else:
            return w(70, 70, 70)

    elif a < b < c:
        r1, r2, r3 = 0, 0, 0
        if wN[a][b][c-1]:
            r1 = wN[a][b][c-1]
        else:
            r1 = w(a, b, c - 1)
        if wN[a][b-1][c-1]:
            r2 = wN[a][b-1][c-1]
        else:
            r2 = w(a, b-1, c - 1)
        if wN[a][b-1][c]:
            r3 = wN[a][b-1][c]
        else:
            r3 = w(a, b-1, c)
        wN[a][b][c] = r1 + r2 - r3
        return r1 + r2 - r3

    else:
        r1, r2, r3, r4 = 0, 0, 0, 0
        if wN[a-1][b][c]:
            r1 = wN[a-1][b][c]
        else:
            r1 = w(a-1, b, c)
        if wN[a-1][b-1][c]:
            r2 = wN[a-1][b - 1][c]
        else:
            r2 = w(a-1, b - 1, c)
        if wN[a-1][b][c-1]:
            r3 = wN[a-1][b][c-1]
        else:
            r3 = w(a-1, b, c-1)
        if wN[a - 1][b-1][c - 1]:
            r4 = wN[a - 1][b-1][c - 1]
        else:
            r4 = w(a - 1, b-1, c - 1)
        wN[a][b][c] = r1 + r2 + r3 - r4
        return r1 + r2 + r3 - r4


wN = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]
for a in range(0, 51):
    for b in range(0, 101):
        for c in range(0, 101):
            wN[a][b][c] = 1
            wN[b][a][c] = 1
            wN[c][b][a] = 1


while True:
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    if x != -1 or y != -1 or z != -1:
        print(f'w({x}, {y}, {z}) = {w(x+50, y+50, z+50)}')
    else:
        break