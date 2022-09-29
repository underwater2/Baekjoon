import math
import re

def trans(n, k):
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    return base[::-1]


def primenum(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    num = trans(n, k)
    li = re.split('0+', num)
    answer = 0
    for l in li:
        if l and primenum(int(l)):
            answer += 1
    return answer