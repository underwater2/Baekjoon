answer = 987654321

def solution(name):
    def move(now, moving, visit):
        global answer
        # 탐색 완료
        if not visit:
            if moving < answer:
                answer = moving
            return
        # 거리 재기        
        distance = [0] * len(visit)
        for idx, v in enumerate(visit):
            temp = abs(v-now)
            if temp > len(cnt)//2:
                temp = len(cnt) - temp
            distance[idx] = temp
        # 순회하기
        for idx, dist in enumerate(distance):
            move(visit[idx], moving+distance[idx], visit[:idx]+visit[idx+1:])
    
    
    cnt = [0] * len(name)
    for idx, char in enumerate(name):
        temp = ord(char)-65
        if temp > 13:
            temp = 26-temp
        cnt[idx] = temp
    if 0 not in cnt:
        return sum(cnt)+len(name)-1
    elif sum(cnt) == 0:
        return 0
    else:
        visit = []
        for idx, c in enumerate(cnt):
            if c and idx:
                visit.append(idx)
        # 재귀로 완전탐색
        now = 0
        moving = 0
        move(now, moving, visit)    
    return sum(cnt)+answer



    