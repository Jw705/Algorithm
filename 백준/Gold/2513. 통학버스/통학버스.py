import sys
from collections import deque

input = sys.stdin.readline

n, k, s = map(int, input().split())

data = []
left_apartment = deque([])
right_apartment = deque([])

for _ in range(n):
    locate, students = map(int, input().split())
    data.append([locate, students])

data.sort(key=lambda x: x[0])

# 학교에서 먼 아파트가 큐의 맨 앞으로 오도록 저장
for locate, students in data:
    if locate < s:
        left_apartment.append([locate, students])
    else:
        right_apartment.appendleft([locate, students])


result = 0

while left_apartment or right_apartment:

    students_on_bus = 0
    max_distance = 0
    while left_apartment and students_on_bus < k:
        locate, students = left_apartment[0]
        # 다 태워도 버스 정원보다 작으면
        if students_on_bus + students <= k:
            left_apartment.popleft()
            students_on_bus += students
            max_distance = max(max_distance, s - locate)
        # 버스 정원을 초과하면 일단 태울 수 있는 학생만큼 다 태운다.
        else:
            left_apartment[0][1] -= (k - students_on_bus)
            students_on_bus = k
            max_distance = max(max_distance, s - locate)

    result += (max_distance * 2)

    students_on_bus = 0
    max_distance = 0
    while right_apartment and students_on_bus < k:
        locate, students = right_apartment[0]
        if students_on_bus + students <= k:
            right_apartment.popleft()
            students_on_bus += students
            max_distance = max(max_distance, locate - s)
        # 버스 정원을 초과하면 일단 태울 수 있는 학생만큼 다 태운다.
        else:
            right_apartment[0][1] -= (k - students_on_bus)
            students_on_bus = k
            max_distance = max(max_distance, locate - s)
    result = result + (max_distance * 2)

print(result)
