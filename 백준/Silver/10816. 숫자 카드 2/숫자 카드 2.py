import sys

N = int(sys.stdin.readline())
mine = list(sys.stdin.readline().split())
M = int(sys.stdin.readline())
search = list(sys.stdin.readline().split())

ans = []
cards = dict()

for i in mine:
    if i not in cards.keys():
        cards[i] = 1
    else:
        cards[i] += 1

for j in search:
    if j in cards.keys():
        ans.append(cards[j])
    else:
        ans.append(0)

print(*ans)