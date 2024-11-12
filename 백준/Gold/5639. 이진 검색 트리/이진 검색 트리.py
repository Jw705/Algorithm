import sys

sys.setrecursionlimit(10 ** 6)

graph = []
while True:
    try:
        graph.append(int(input()))
    except:
        break


# graph = [50, 30, 24, 5, 28, 45, 98, 52, 60]


def postorder(s, e):
    if s > e:
        return
    mid = e + 1  # 오른쪽 노드 없을 경우

    for i in range(s + 1, e + 1):
        if graph[s] < graph[i]:
            mid = i
            break

    postorder(s + 1, mid - 1)  # 왼쪽 확인
    postorder(mid, e)  # 오른쪽 확인
    print(graph[s])


postorder(0, len(graph) - 1)
