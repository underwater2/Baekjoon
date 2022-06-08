import sys

def dfs(start):
    global amount, result

    # if N == 1 and tp[1][0] != 1:
    #     result = 0
    #     return
    #
    # if start == N and tp[N][0] != 1:
    #     result = 0
    #     return

    if start + tp[start][0] <= N+1:
        amount += tp[start][1]  # 더하기 전에, 유효한 값인지 확인해야할듯
    result = max(amount, result)
    for i in range(start + tp[start][0], N+1):
        if i + tp[i][0] <= N+1:
            dfs(i)
            amount -= tp[i][1]


N = int(sys.stdin.readline())

tp = [0]
for _ in range(N):
    tp.append(list(map(int, sys.stdin.readline().split())))

res = 0

for i in range(1, N+1):
    amount, result = 0, 0
    dfs(i)
    res = max(res, result)

print(res)