import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

arr = [0 for _ in range(m)]
answer = 0

for i in range(2, m):
    if s[i] == 'I' and s[i - 1] == 'O' and s[i - 2] == 'I':
        arr[i] = arr[i - 2] + 1
        if arr[i] >= n:
            answer += 1

print(answer)