dp = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def solution(n):
    for i in range(len(dp), n+1):
        dp.append((dp[i-1] + dp[i-2]) % 1000000007) 
    return dp[n]