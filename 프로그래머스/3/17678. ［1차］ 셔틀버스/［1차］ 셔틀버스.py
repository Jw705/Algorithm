# 47m
from collections import deque

# 주어진 시간이 셔틀을 탈 수 있는 시간인지 확인
def is_last_time(parsed_timetable, target, n, m, t):
    # 셔틀 대기열에 target 시간 추가 후 정렬
    queue = deque(sorted(parsed_timetable.copy() + [target]))
    cur_time = 9 * 60
    while cur_time < 24 * 60 and n > 0 and len(queue) > 0:
        for _ in range(m):
            if queue[0] <= cur_time:
                queue.popleft()
            if len(queue) == 0:
                break
        cur_time += t
        n -= 1

    if len(queue) == 0 or target < queue[0]:
        return True
    else:
        return False


def solution(n, t, m, timetable):
    # 시간을 분 단위로 변환
    parsed_timetable = []
    for time in timetable:
        hh, mm = map(int, time.split(":"))
        parsed_timetable.append(hh * 60 + mm)

    # 이진 탐색으로 정답시간 계산
    answer_time = 24 * 60
    l = 0
    r = 24 * 60 - 1
    while l <= r:
        mid = (l + r) // 2
        if is_last_time(parsed_timetable, mid, n, m, t):
            answer_time = mid
            l = mid + 1
        else:
            r = mid - 1

    # 정답시간을 HH:MM 형식으로 변환해서 반환
    hh = answer_time // 60
    mm = answer_time % 60
    answer = f"{hh:02}:{mm:02}"

    return answer