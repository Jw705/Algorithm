import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()


def find_sequence(arr):
    if len(arr) == m:
        for a in arr:
            print(data[a], end=' ')
        print('')
    else:
        prev = -1
        for i in range(n):
            if i not in arr and data[i] != prev:
                prev = data[i]
                arr.append(i)
                find_sequence(arr)
                arr.pop()


prev = -1
for i in range(n):
    if data[i] != prev:
        prev = data[i]
        find_sequence([i])