import sys

n = int(sys.stdin.readline())
all_num = list(map(int, sys.stdin.readline().split()))
all_num.sort()

m = int(sys.stdin.readline())
want_num = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    elif target > mid:
        return binary_search(arr, target, mid + 1, end)
    elif target < mid:
        return binary_search(arr, target, start, mid - 1)
    return None


for i in range(m):
    res = binary_search(all_num, want_num[i], 0, n - 1)
    if res == None:
        print("no", end=" ")
    else:
        print("yes", end=' ')

'''
5
8 3 7 9 2
3
5 7 9
'''
