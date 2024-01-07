n, m = map(int, input().split())

a, b, d = map(int, input().split())

map_info = []

for _ in range(m):
    map_info.append(list(map(int, input().split())))

map_info[a][b] = -1

# 여기가 핵심! 방향 문제는 이런 식으로 배열 만들면 편해진다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit_cnt = 1
rotate_cnt = 0

while True:
    # 회전
    if d == 0:
        d = 3
    else:
        d -= 1
    rotate_cnt += 1

    # 탐색
    if map_info[a + dx[d]][b + dy[d]] == 0:
        map_info[a + dx[d]][b + dy[d]] = -1
        a = a + dx[d]
        b = b + dy[d]
        visit_cnt += 1
        rotate_cnt = 0

    if rotate_cnt == 4:
        d = (d + 2) % 4
        if map_info[a + dx[d]][b + dy[d]] == 1:
            break
        rotate_cnt = 0

print(visit_cnt)

'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

3


while True:
    # 회전
    if d == 0:
        d = 3
    else:
        d -= 1
    rotate_cnt += 1

    # 탐색
    if d == 0:
        if map_info[a - 1][b] == 0:
            map_info[a - 1][b] = -1
            a -= 1
            visit_cnt += 1
            rotate_cnt = 0
    if d == 1:
        if map_info[a][b + 1] == 0:
            map_info[a][b + 1] = -1
            b += 1
            visit_cnt += 1
            rotate_cnt = 0
    if d == 2:
        if map_info[a + 1][b] == 0:
            map_info[a + 1][b] = -1
            a += 1
            visit_cnt += 1
            rotate_cnt = 0
    if d == 3:
        if map_info[a][b - 1] == 0:
            map_info[a][b - 1] = -1
            b -= 1
            visit_cnt += 1
            rotate_cnt = 0

    if rotate_cnt == 4:
        d = (d + 2) % 4
        if d == 0:
            if map_info[a - 1][b] == 1:
                break
        if d == 1:
            if map_info[a][b + 1] == 1:
                break
        if d == 2:
            if map_info[a + 1][b] == 1:
                break
        if d == 3:
            if map_info[a][b - 1] == 1:
                break
        rotate_cnt = 0
'''
