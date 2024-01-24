import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()

m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return None


for i in mlist:
    if binary_search(nlist, i, 0, len(nlist) - 1):
        print(1)
    else:
        print(0)

'''
5
4 1 5 2 3
5
1 3 7 9 5
'''
