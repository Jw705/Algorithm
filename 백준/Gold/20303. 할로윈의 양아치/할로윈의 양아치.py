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
for i in range(n):
    tmp = find_parent(parent, i + 1)
    if tmp not in data:
        data[tmp] = {'child_num': 1, 'candy_num': candies[i]}
    else:
        data[tmp]['child_num'] = data[tmp]['child_num'] + 1
        data[tmp]['candy_num'] = data[tmp]['candy_num'] + candies[i]

arr = [[0, 0]]
for d in data.values():
    arr.append([d['child_num'], d['candy_num']])

group_num = len(arr)
dp = [0 for _ in range(k)]

for i in range(1, group_num):
    for j in range(k - 1, 0, -1):
        w, v = arr[i]
        if j >= w:
            dp[j] = max(dp[j], dp[j - w] + v)
            
print(dp[k - 1])
