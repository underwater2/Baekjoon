def solution(n,a,b):
    answer = 1
    if a > b:  a,b = b,a 
    while True:
        if b-a == 1 and (a+1)//2 == (b+1)//2:
            return answer
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
    # return answer