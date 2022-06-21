import sys

import heapq

N = int(sys.stdin.readline().rstrip())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline().rstrip()))
ans = 0
while len(cards) != 1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    AB = A + B
    ans += AB
    heapq.heappush(cards, AB)
print(ans)
