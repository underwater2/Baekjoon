import sys
import math

n1, n2 = map(int, sys.stdin.readline().rstrip().split())

print(math.gcd(n1, n2))
print(math.lcm(n1, n2))