from collections import Counter

def solution(nums):
    maxN = len(nums)//2
    num = Counter(nums)
    if maxN <= len(num.keys()):
        return maxN
    else:
        return len(num.keys())