n = int(input())
arr = list(map(int, input().split()))
m = int(input())

result = 0
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for a in arr:
        if a > mid:
            total += mid
        else:
            total += a

    if total <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)