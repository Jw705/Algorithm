import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

hole = [0] * n

ans = 0

for i in range(k):

    # 빈 구멍이 있거나 이미 꽂혀 있는지 확인
    isPluggedIn = False
    for j in range(n):
        if hole[j] == data[i] or hole[j] == 0:
            hole[j] = data[i]
            isPluggedIn = True
            break

    # 빈 구멍이 없으면
    if not isPluggedIn:
        # 희생될 플러그 정보 [idx, last_use]
        victim = [0, 0]

        # 구멍을 전체 순회하면서 희생될 플러그 찾기
        for j in range(n):
            last_use = k + 1

            # 해당 구멍에 꽂혀있는 플러그가 언제 마지막으로 다시 필요한지 확인
            for l in range(i, k):
                if data[l] == hole[j]:
                    last_use = l
                    break

            # 희생될 플러그보다 현재 플러그가 더 나중에 필요하면
            if last_use > victim[1]:
                # 현재 플러그를 뽑는다.
                victim = [j, last_use]

        hole[victim[0]] = data[i]
        ans += 1

print(ans)