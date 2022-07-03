import sys

import math

A, B, V = map(int, sys.stdin.readline().rstrip().split())

goal = V-A
multi = A-B
ans = math.ceil(goal / multi)
print(ans+1)