def recursion(n, num):
    if (n-1)//3 < 0:
        return num
    cond = (n-1)%3
    if cond == 0:
        num = '1' + num
    elif cond == 1:
        num = '2' + num
    else:
        num = '4' + num
    return recursion((n-1)//3, num)
    

def solution(n):
    num = ''
    answer = recursion(n, num)
 
    
    # # dp - 시간초과
    # nums = [0] * (166666667)
    # nums[1], nums[2], nums[3] = 1, 2, 4
    # end = 0
    # if n > 166666666:
    #     end = 166666666
    # else:
    #     end = n+3
    # for i in range(4, end, 3):
    #     front = str(nums[i//3])
    #     nums[i], nums[i+1], nums[i+2] = int(front+'1'), int(front+'2'), int(front+'4')
    # answer = str(nums[n])
    return answer