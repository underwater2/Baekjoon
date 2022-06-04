import sys

from itertools import permutations

def calc(n1, n2, oper):
    if oper == 0:
        return n1 + n2
    elif oper == 1:
        return n1 - n2
    elif oper == 2:
        return n1 * n2
    elif oper == 3:
        if n1 < 0:
            temp = -n1 // n2
            return -temp
        return n1 // n2


N = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
newo = []
for i in range(4):
    newo.extend([i] * operator[i])

minV = 987654321
maxV = -987654321

perms = set(list(permutations(newo, len(newo))))
for perm in perms:
    # print(perm)
    result = calc(num[0], num[1], perm[0])
    for j in range(2, N):
        result = calc(result, num[j], perm[j-1])
    # print(result)
    if result > maxV:
        maxV = result
    if result < minV:
        minV = result

print(maxV)
print(minV)