import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def find_sequence(arr):
    if len(arr) == m:
        print(*arr)
    else:
        last = arr[len(arr) - 1]
        for j in range(last + 1, n + 1):
            arr.append(j)
            find_sequence(arr)
            arr.pop()


for i in range(1, n + 1):
    find_sequence([i])