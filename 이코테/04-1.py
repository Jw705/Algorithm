N = int(input())

move_list = list(input().split())

coordinate = [1, 1]

for move in move_list:
    if move == 'L':
        if coordinate[1] > 1: coordinate[1] -= 1
    elif move == 'R':
        if coordinate[1] < N: coordinate[1] += 1
    elif move == 'U':
        if coordinate[0] > 1: coordinate[0] -= 1
    elif move == 'D':
        if coordinate[0] < N: coordinate[0] += 1

print(coordinate[0], coordinate[1])

'''
5
R R R U D D
'''
