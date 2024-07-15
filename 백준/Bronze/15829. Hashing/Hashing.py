import sys

input = sys.stdin.readline

l = int(input())
data = input()

result = 0

for i in range(l):
    result += ((ord(data[i]) - 96) * (31 ** i))

print(result)