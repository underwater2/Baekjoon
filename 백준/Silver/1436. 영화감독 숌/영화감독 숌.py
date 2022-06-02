import sys

N = int(sys.stdin.readline())

order = 0
for i in range(666, 987654321):
    for s in range(0, len(str(i))-2):
        if str(i)[s:s+3] == '666':
            order += 1
            if order == N:
                print(i)
                exit()
            break