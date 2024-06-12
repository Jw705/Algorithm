import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = dict()

for _ in range(n):
    site, password = input().split()
    data[site] = password

for _ in range(m):
    print(data[input().rstrip()])