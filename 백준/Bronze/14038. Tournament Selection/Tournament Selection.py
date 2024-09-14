import sys

input = sys.stdin.readline

win_count = 0
for _ in range(6):
    result = input().rstrip()
    if result == 'W':
        win_count += 1

if win_count >= 5:
    print(1)
elif win_count >= 3:
    print(2)
elif win_count >= 1:
    print(3)
else:
    print(-1)