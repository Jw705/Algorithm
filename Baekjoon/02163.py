N, M = map(int, input().split(' '))

max, min = max(N, M), min(N, M)

cnt = 0
cnt += min-1
cnt += (max-1)*min

print(cnt)