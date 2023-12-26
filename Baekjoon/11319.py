N = int(input())

data = list(map(int, input().split()))
data.sort()

res = 0

for i in range(N):
    res += sum(data[0:i]) + data[i]

print(res)

"""
5
3 1 4 3 2
"""
