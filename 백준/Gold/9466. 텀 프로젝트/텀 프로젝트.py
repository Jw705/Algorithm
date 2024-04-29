import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data.insert(0, 0)
    visited = [False] * (n + 1)

    result = n

    for j in range(1, len(data)):
        if not visited[j]:
            current_idx = j
            team_list = {j: 0}
            while True:
                next_idx = data[current_idx]
                visited[current_idx] = True

                if next_idx in team_list:
                    result -= (len(team_list) - team_list[next_idx])
                    break

                if visited[next_idx]:
                    break

                current_idx = next_idx
                team_list[current_idx] = len(team_list)

    print(result)

'''
1
4
2 3 4 2

2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''
