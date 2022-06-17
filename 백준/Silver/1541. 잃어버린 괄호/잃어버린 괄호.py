import sys

calc = sys.stdin.readline()

calc_list = []
num = ''
for c in calc:
    if c != "+" and c != "-":
        num += c
    else:
        calc_list.append(num)
        num = ''
        calc_list.append(c)
calc_list.append(num)

result = int(calc_list[0])
calc_list = calc_list[1:]
temp = 0
for el in range(len(calc_list)-1, -1, -2):
    if calc_list[el-1] == '+':
        temp += int(calc_list[el])
    else:
        temp += int(calc_list[el])
        result -= temp
        temp = 0
print(temp + result)
