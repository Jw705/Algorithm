import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

hole = [0] * n

# print(data)
# print(hole)

ans = 0

for i in range(k):
    isPluggedIn = False
    for j in range(n):
        if hole[j] == data[i] or hole[j] == 0:
            hole[j] = data[i]
            isPluggedIn = True
            break
    if not isPluggedIn:
        #print(data[i], "찾는다")
        victim = [0, 0]
        for j in range(n):

            last_use = k + 1
            for l in range(i, k):
                if data[l] == hole[j]:
                    last_use = l
                    break

            if last_use > victim[1]:
                victim = [j, last_use]

            #print(data[j], last_use)
        #print(victim, data[victim[0]])
        hole[victim[0]] = data[i]
        ans += 1

    #print(hole)
print(ans)

'''
2 9
1 2 3 1 2 3 1 2 3

3 13
2 3 4 2 3 4 1 5 5 5 2 3 2

3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4

2 4
5 3 1 5

3 100
56 71 70 25 52 77 76 8 68 71 51 65 13 23 7 16 19 54 95 18 86 74 29 76 61 93 44 96 32 72 64 19 50 49 22 14 7 64 24 83 6 3 2 76 99 7 76 100 60 60 6 50 90 49 27 51 37 61 16 84 89 51 73 28 90 77 73 39 78 96 78 13 92 54 70 69 62 78 7 75 30 67 97 98 19 86 90 90 2 39 41 58 57 84 19 8 52 39 26 7
'''
