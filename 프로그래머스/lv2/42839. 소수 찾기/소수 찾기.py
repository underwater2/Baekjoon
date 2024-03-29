from itertools import permutations

def solution(numbers):
    num = []
    # 한 숫자씩 자르기
    for number in numbers:
        num.append(number)
    # 순열로 구한 숫자들을 set에 넣기
    setnums = set()
    for i in range(1, len(num)+1):
        for perm in permutations(num, i):
            elem = ''
            for n in perm:
                elem += n
            setnums.add(int(elem))
    print(setnums)
    # 소수인지 판별
    answer = 0
    for n in setnums:
        if is_decimal(n):
            answer += 1
    return answer


def is_decimal(x):  # 소수면 True 반환
    if x == 1 or x == 0:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    return True