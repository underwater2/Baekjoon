import sys

price = int(input())
change = 1000 - price
cnt = 0
coin = [500, 100, 50, 10, 5, 1]

while change > 0:
    for c in coin:
        if change >= c:
            cnt += change // c
            change %= c
            break

print(cnt)