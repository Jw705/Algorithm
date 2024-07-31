import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

start = min(data)
answer = end = max(data) * m

while start <= end:
    mid = (start + end) // 2

    total = 0  # mid시간 동안 검사할 수 있는 총 사람의 수
    for i in range(n):
        total += mid // data[i]

    if total >= m:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)