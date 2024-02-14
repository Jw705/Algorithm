n, m = map(int, input().split())

d = [20000] * 10001

arr = []
for _ in range(n):
    data = int(input())
    arr.append(data)
    d[data] = 1

for i in range(1, m + 1):
    for j in range(n):
        if i - arr[j] > 0:
            print([i, arr[j]], d[i], d[i - arr[j]])
            d[i] = min(d[i], d[i - arr[j]] + 1)

if d[m] == 20000:
    print(-1)
else:
    print(d[m])

'''
2 15
2
3

3 4
3
5
7
'''
