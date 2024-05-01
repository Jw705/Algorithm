import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
candies = list(map(int, input().split()))

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# O(m)
for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

data = {}

# O(n)
for i in range(n):
    tmp = find_parent(parent, i + 1)
    if tmp not in data:
        data[tmp] = [1,candies[i]]
    else:
        data[tmp][0] = data[tmp][0] + 1
        data[tmp][1] = data[tmp][1] + candies[i]

# print(data)

arr = [[0, 0]]
for d in data.values():
    arr.append(d)

# print(arr)

group_num = len(arr)

dp = [[0] * k for _ in range(group_num)]

for i in range(1, group_num):
    for j in range(1, k):
        w, v = arr[i]
        if j >= w:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

# print(dp)
print(dp[group_num - 1][k - 1])

'''
10 6 6
9 15 4 4 1 5 19 14 20 5
1 3
2 5
4 9
6 2
7 8
6 10

5 4 4
9 9 9 9 9
1 2
2 3
3 4
4 5
'''
