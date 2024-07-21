import sys

input = sys.stdin.readline

n, m = map(int, input().split())

듣못사 = {}
듣보잡 = []

for _ in range(n):
    듣못사[input().rstrip()] = True

for _ in range(m):
    data = input().rstrip()
    if data in 듣못사:
        듣보잡.append(data)

듣보잡.sort()

print(len(듣보잡))
for 듣보 in 듣보잡:
    print(듣보)
