def solution(arr):
    stack = [arr[0]]
    
    former = arr[0]
    for i in range(1, len(arr)):
        if former == arr[i]:
            continue
        stack.append(arr[i])
        former = arr[i]
    return stack