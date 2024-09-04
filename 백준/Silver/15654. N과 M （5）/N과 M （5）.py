import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()


def find_sequence(arr):
    if len(arr) == m:
        print(*arr)
    else:
        for d in data:
            if d not in arr:
                arr.append(d)
                find_sequence(arr)
                arr.pop()


for d in data:
    find_sequence([d])