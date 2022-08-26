def solution(number, k):
    num = list(number)
    temp = []
    for i in range(len(num)-1):
        temp.append(i)
        if num[i] < num[i+1]:
            for t in temp:
                num[t] = 0
        elif num[i] == num[i+1]:
    print(num)
    answer = ''
    return answer