import sys

N = int(sys.stdin.readline().rstrip())

alphabet = dict()

for _ in range(N):
    voca = sys.stdin.readline().rstrip()
    num = 1
    for idx in range(len(voca)-1, -1, -1):
        if voca[idx] in alphabet:
            alphabet[voca[idx]] += num
        else:
            alphabet[voca[idx]] = num
        num *= 10

alphabet_sorted = sorted(alphabet.values(), reverse=True)
nn = 9
ans = 0
for al in alphabet_sorted:
    ans += nn * al
    nn -= 1
print(ans)