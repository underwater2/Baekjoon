import sys

N = int(sys.stdin.readline().rstrip())

stair = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(N)]

dp = [0 for _ in range(N+1)] # 진최댓값
exdp = [0 for _ in range(N+1)] # 전 계단 제외 최댓값

dp[1] = stair[1]
exdp[1] = stair[1]

if N > 1:
    dp[2] = stair[1] + stair[2]
    exdp[2] = stair[2]

    for i in range(3, N+1):
        exdp[i] = dp[i-2]+stair[i]
        dp[i] = max(stair[i]+exdp[i-1], stair[i]+dp[i-2])

print(dp[N])