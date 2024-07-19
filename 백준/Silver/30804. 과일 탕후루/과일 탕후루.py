import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

answer = 0
kind = {data[0]: 1}
left, right = 0, 1

while right < n:
    if len(kind) > 2:
        kind[data[left]] -= 1
        if kind[data[left]] == 0:
            del kind[data[left]]
        left += 1
    else:
        if len(kind) == 2:
            answer = max(answer, right - left)

        if data[right] in kind:
            kind[data[right]] += 1
        else:
            kind[data[right]] = 1
        right += 1

if len(kind) <= 2:
    answer = max(answer, right - left)
print(answer)