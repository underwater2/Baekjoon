import heapq

def solution(jobs):
    # li = [[12, 0],[0, 6], [0,2], [1,3], [1, 0], [2, 11], [2,3]]
    # li = [[0, 3], [12, 1]]
    # li = [[0,1],[1,2],[2,3]]
    # li = [[12,1], [0,3]]
    # li = [[5, 10], [6, 8], [14, 2], [11, 5], [100, 7]]
    # li = [[0, 10], [4, 10], [5, 11], [15, 2]]
    # li = [[0, 16], [0, 14], [15, 1], [13, 13]]
    # li = [[0, 10], [4, 10], [15, 2], [5, 11]]
    # li = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
    sjobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    # print(sjobs)
    count = len(sjobs)
    h = []
    now = 0
    answer = 0
    while sjobs:
        while sjobs[-1][0] <= now:
            heapq.heappush(h, sjobs.pop()[::-1])
            if not sjobs:
                break
        if h:
            req = heapq.heappop(h)
            print("heapq", req)
            now += req[0]
            print("now", now)
            answer += now - req[1]
            print("sum", answer)
        else:
            now += 1
    while h:
        req = heapq.heappop(h)
        print("heapq", req)
        now += req[0]
        print("now", now)
        answer += now - req[1]
        print("sum", answer)
    # print("now", now)
    # print("sum", answer)
    # print("answer", int(answer/count))
    answer = answer//count
    print(answer)

    return answer