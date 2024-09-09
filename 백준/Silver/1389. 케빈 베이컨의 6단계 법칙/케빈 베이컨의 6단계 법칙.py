import sys

# 입력 받기
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 큰 값 설정

# 노드와 간선의 수 입력 받기
n, m = map(int, input().split())

# 그래프 초기화 (모든 값을 무한으로 초기화)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 경로는 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1  # 서로 연결된 간선의 가중치는 1
    graph[b][a] = 1  # 양방향이므로 대칭적으로 처리

# 플로이드-워셜 알고리즘으로 모든 노드 간 최단 거리 계산
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 케빈 베이컨 수가 가장 작은 사람 찾기
min_kevin_bacon = INF  # 최소 케빈 베이컨 수
answer = -1  # 답을 저장할 변수

for person in range(1, n + 1):
    kevin_bacon = sum(graph[person][1:n+1])  # 해당 사람의 케빈 베이컨 수 계산
    
    if kevin_bacon < min_kevin_bacon:
        min_kevin_bacon = kevin_bacon
        answer = person

# 결과 출력
print(answer)