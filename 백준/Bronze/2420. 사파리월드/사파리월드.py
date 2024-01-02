a, b = map(int, input().split())

res = a-b

if res<0:
    print(-1*res)
else:
    print(res)