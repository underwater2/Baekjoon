from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)

    sec = 0
    w = 0
    while True:
        sec += 1
        if not truck and sum(bridge) == 0:
            break
        out_truck = bridge.popleft()
        w -= out_truck
        if truck and (w + truck[0]) <= weight:
            next_truck = truck.popleft()
            w += next_truck
            bridge.append(next_truck)
        else:
            bridge.append(0)
    return sec-1