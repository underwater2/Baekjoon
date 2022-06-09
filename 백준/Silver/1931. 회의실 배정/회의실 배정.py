import sys

N = int(sys.stdin.readline())

meeting = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))

meeting = sorted(meeting)
start_time = meeting[0][0]
end_time = meeting[0][1]
result = 1
for i in meeting[1:]:
    if end_time <= i[0]:
        result += 1
        start_time = i[0]
        end_time = i[1]

    if end_time > i[1]:
        start_time = i[0]
        end_time = i[1]


print(result)