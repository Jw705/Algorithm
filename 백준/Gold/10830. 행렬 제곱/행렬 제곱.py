import sys

input = sys.stdin.readline


def matrix_multiplication(a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j] % 1000
    return result


def square(x, n):  # 분할 정복을 이용해 요구 사항만큼 제곱하기
    if n == 1:
        return x
    temp = square(x, n // 2)
    if n % 2 == 0:
        return matrix_multiplication(temp, temp)
    else:
        return matrix_multiplication(matrix_multiplication(temp, temp), x)


n, b = map(int, input().split())
matrix = []

for _ in range(n):
    data = list(map(int, input().split()))
    matrix.append(data)

answer = square(matrix, b)

for i in range(n):
    for j in range(n):
        print(answer[i][j] % 1000, end=' ')
    print()
