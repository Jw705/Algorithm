N, K = map(int, input().split(' '))

data = []
for _ in range(N):
    data.append(int(input()))

res = 0
data.sort(reverse=True)
for i in range(N):
    if data[i] <= K:
        res += K // data[i]
        K = K % data[i]

print(res)

'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

10 4790
1
5
10
50
100
500
1000
5000
10000
50000
'''
