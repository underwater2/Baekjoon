import sys

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
cnt_coin = 0

for i in range(N-1, -1, -1):

    if K >= coin[i]:
        cnt_coin += K // coin[i]
        K %= coin[i]

    if K == 0:
        print(cnt_coin)
        break

