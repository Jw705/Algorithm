import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * 41

for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i + j] += 1

max_sum = max(arr)

for i in range(41):
    if arr[i] == max_sum:
        print(i)