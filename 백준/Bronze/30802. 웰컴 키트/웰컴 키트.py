import sys

input = sys.stdin.readline

n = int(input())
tmp = n

shirt_data_list = list(map(int, input().split()))
t, p = map(int, input().split())

shirt_bundle = 0

for s in shirt_data_list:
    if s == 0:
        continue
    elif s > t:
        shirt_bundle += s // t
        if s % t > 0:
            shirt_bundle += 1
    else:
        shirt_bundle += 1

print(shirt_bundle)
print(n // p, n % p)