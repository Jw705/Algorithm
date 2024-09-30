import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
치킨거리 = [[] for _ in range(m)]
normal_houses = []
chicken_houses = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            normal_houses.append([i,j])
        if graph[i][j] == 2:
            chicken_houses.append([i,j])

selected = list(combinations(range(len(chicken_houses)), m))

answer = 1e9

for 현재조합 in selected:
    치킨거리합 = 0
    for house in normal_houses:
        최소치킨거리 = 1e9
        for 치킨집index in 현재조합:
            최소치킨거리 = min(최소치킨거리, abs(house[0] - chicken_houses[치킨집index][0]) + abs(house[1] - chicken_houses[치킨집index][1]))
        치킨거리합 += 최소치킨거리
    answer = min(answer, 치킨거리합)

print(answer)