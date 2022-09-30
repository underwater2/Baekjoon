def trans(n, k):  # 숫자 n, k진법
    result = ''
    alphabet = list('ABCDEF')
    while n > 0:
        n, mod = divmod(n, k)
        if (mod-10) >= 0:
            result += alphabet[mod-10]
        else:
            result += str(mod)
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    game = '01'
    now = 2
    while len(game) < p+(t-1)*m:
        game += trans(now, n)
        now += 1
    for i in range(p-1, p+(t-1)*m, m):
        answer += game[i]
    return answer