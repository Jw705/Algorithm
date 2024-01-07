position = input()

coordinate = [ord(position[0]) - ord("a") + 1, int(position[1])]

cnt = 0

if coordinate[0] + 2 <= 8:
    if coordinate[1] + 1 <= 8: cnt += 1
    if coordinate[1] - 1 > 0: cnt += 1
if coordinate[0] - 2 > 0:
    if coordinate[1] + 1 <= 8: cnt += 1
    if coordinate[1] - 1 > 0: cnt += 1
if coordinate[1] + 2 <= 8:
    if coordinate[0] + 1 <= 8: cnt += 1
    if coordinate[0] - 1 > 0: cnt += 1
if coordinate[1] - 2 > 0:
    if coordinate[0] + 1 <= 8: cnt += 1
    if coordinate[0] - 1 > 0: cnt += 1

print(cnt)

cnt = 0
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
for step in steps:
    x, y = coordinate[0] + step[0], coordinate[1] + step[1]
    if x > 0 and y > 0 and x <= 8 and y <= 8: cnt += 1

print(cnt)

'''
a1

2
'''
