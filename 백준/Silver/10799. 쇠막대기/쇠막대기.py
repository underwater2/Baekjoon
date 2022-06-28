import sys

stick = sys.stdin.readline().rstrip()

idx = 0
cnt = 0
ans = 0
while idx < len(stick):
    elem = stick[idx]
    if elem == ')':
        cnt -= 1
        idx += 1
        
    elif elem == '(':
        if stick[idx+1] == ')':
            ans += cnt
            idx += 2
        else:
            ans += 1
            cnt += 1
            idx += 1

print(ans)