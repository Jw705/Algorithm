import sys

input = sys.stdin.readline

n = int(input())

result = 0
for i in range(1, n+1):
    num = str(i)
    result += (num.count('3')) + (num.count('6')) + (num.count('9'))

print(result)
