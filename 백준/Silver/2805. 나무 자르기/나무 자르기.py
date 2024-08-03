import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

answer = start = 1
end = max(data)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for d in data:
        if d >= mid:
            total += d - mid

    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)