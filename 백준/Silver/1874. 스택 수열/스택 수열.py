import sys

from collections import deque

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]

def calc(num):
    temp = deque()
    nowN = 1
    pp = deque()

    for i in num:
        if i >= nowN:
            for j in range(nowN, i):
                temp.append(nowN)
                nowN += 1
                pp.append('+')
            nowN += 1
            pp.append('+')
            pp.append('-')
        else:
            while True:
                outN = temp.pop()
                pp.append('-')
                if outN != i:
                    pp = ['NO']
                    return pp
                else:
                    break
    return pp


for p in calc(num):
    print(p)