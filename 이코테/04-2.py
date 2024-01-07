N = int(input())

cnt = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if i == 3 or i == 13:
                cnt += 1
            elif j % 10 == 3 or j // 10 == 3:
                cnt += 1
            elif k % 10 == 3 or k // 10 == 3:
                cnt += 1

print(cnt)

cnt = 0
for i in range(N+1):
    if i == 3 or i == 13:
        cnt += 60*60
    else:
        cnt += 15*60 + 45*15

print(cnt)

'''
5

11475


3 13 23 43 53 5개
30-39 10개
15개

15*60 + 45*15
'''
