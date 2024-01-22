import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    tmp_sum = 0
    for i in range(mid, len(arr)):
        tmp_sum += arr[i] - arr[mid]

    if target == tmp_sum:
        return arr[mid]
    elif target < tmp_sum:
        return binary_search(arr, target, mid + 1, end)
    elif target > tmp_sum:
        return binary_search(arr, target, start, mid - 1)
    return None


res = binary_search(data, m, 0, n)
print(res)

'''
4 6
19 15 10 17
'''
