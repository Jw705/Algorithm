import sys

input = sys.stdin.readline

x = int(input())

n = 0
while n ** 2 < x:
    n += 1

for _ in range(n + 2):
    print('x', end='')
print('')
for _ in range(n):
    print('x', end='')
    for _ in range(n):
        print('.', end='')
    print('x', end='')
    print('')
for _ in range(n + 2):
    print('x', end='')