import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())

    if n == 0:
        data = []
        tmp = input()
    else:
        data = list(map(int, input().rstrip().strip('[]').split(',')))

    answer = []

    r_cnt = 0
    d_left_cnt = 0
    d_right_cnt = 0

    for cmd in p:
        if cmd == 'R':
            r_cnt += 1
        elif cmd == 'D':
            if r_cnt % 2 == 0:
                d_left_cnt += 1
                if d_left_cnt + d_right_cnt > len(data):
                    answer = 'error'
            elif r_cnt % 2 == 1:
                d_right_cnt += 1
                if d_left_cnt + d_right_cnt > len(data):
                    answer = 'error'

    if answer == 'error':
        print('error')
        continue

    if r_cnt % 2 == 0:
        i = d_left_cnt
        while i < len(data) - d_right_cnt:
            if data[i] != 0:
                answer.append(data[i])
            i += 1
    elif r_cnt % 2 == 1:
        i = len(data) - 1 - d_right_cnt
        while i >= 0 + d_left_cnt:
            if data[i] != 0:
                answer.append(data[i])
            i -= 1

    print("[" + ",".join(map(str, answer)) + "]")