import sys

input = sys.stdin.readline

n = int(input())
res = 0
arr = [2, 3, 4, 5, 6, 7, 2]
arr2 = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z']

for i in range(7):
    res += n % 10 * arr[i]
    n = n // 10

print(arr2[res % 11])