import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)

for i in range(2, n+1):
    minN = []
    if i % 3 == 0:
        minN.append(1 + dp[i//3])
    if i % 2 == 0:
        minN.append(1 + dp[i//2])
    minN.append(1 + dp[i-1])
    dp[i] = min(minN)

print(dp[n])