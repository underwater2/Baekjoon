def solution(numbers):
    strings = []
    for number in numbers:
        number = str(number)
        plus = 4-len(number)
        while len(number) != 4:
            if len(number) > 4:
                number = number[:4]
            elif len(number) < 4:
                number *= 4
        tup = (number, plus)
        strings.append(tup)
    
    strings = sorted(strings, key=lambda x:x[0], reverse=True)
    answer = ''
    for string in strings:
        answer += string[0][:4-string[1]]
    if answer[0] == '0':  # 반례 [0, 0, 0, 0, 0, 0] "0"
        answer = '0'
    return answer