import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

def LIS(array):
    dp = []  # dp 리스트를 빈 리스트로 초기화
    for num in array:
        # num이 들어갈 위치 찾기
        idx = bisect_left(dp, num)
        # num이 가장 큰 값이면 dp에 추가
        if idx == len(dp):
            dp.append(num)
        else:
            # num이 들어갈 위치의 값을 num으로 대체
            dp[idx] = num
    return len(dp)

print(LIS(data))