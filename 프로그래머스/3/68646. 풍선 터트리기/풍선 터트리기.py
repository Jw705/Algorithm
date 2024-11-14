# 32m

def solution(a):
    answer = 0
    n = len(a)

    # min_start_left[i]는 a[0:i + 1] 중 최소값 저장
    # min_start_right[i]는 a[i:len(a)] 중 최소값 저장
    min_start_left = [0] * n
    min_start_right = [0] * n

    min_start_left[0] = a[0]
    min_start_right[n - 1] = a[n - 1]
    for i in range(1, n):
        min_start_left[i] = min(a[i], min_start_left[i - 1])
    for i in range(n - 2, -1, -1):
        min_start_right[i] = min(a[i], min_start_right[i + 1])

    # 자신 왼쪽과 오른쪽에 자신보다 작은 수가 있으면 마지막까지 남길 수 없다.
    for i in range(n):
        if min_start_left[i] < a[i] and min_start_right[i] < a[i]:
            continue
        answer += 1

    return answer