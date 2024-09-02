import sys

input = sys.stdin.readline

n, m = map(int, input().split())


def find_sequence(arr):
    if len(arr) == 0:
        for i in range(1, n + 1):
            find_sequence([i])
    elif len(arr) == m:
        for a in arr:
            print(a, end=' ')
        print('')
    else:
        last = arr[len(arr) - 1]
        for j in range(last + 1, n + 1):
            new_arr = []
            for a in arr:
                new_arr.append(a)
            new_arr.append(j)
            find_sequence(new_arr)


find_sequence([])