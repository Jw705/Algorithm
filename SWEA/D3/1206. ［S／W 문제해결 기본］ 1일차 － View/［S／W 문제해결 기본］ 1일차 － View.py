T = 10

for test_case in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))
    answer = 0
    for i in range(2, n - 2):
        l_max = max(data[i - 2], data[i - 1])
        r_max = max(data[i + 2], data[i + 1])
        조망권확보세대 = min(data[i] - l_max, data[i] - r_max)
        if 조망권확보세대 > 0:
            answer += 조망권확보세대

    print(f'#{test_case} {answer}')