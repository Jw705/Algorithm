import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
buttons = []
if m > 0:
    buttons = list(map(int, input().split()))

target_ch = n

cnt = 0
cnt2 = 0


def possible_num(num):
    if num == 0 and 0 in buttons:
        return False
    while num > 0:
        tmp = num % 10
        if tmp in buttons:
            return False
        num //= 10
    return True


plus_num = target_ch
minus_num = target_ch

while not possible_num(plus_num):
    plus_num += 1
    if plus_num > 1000000:
        break
while not possible_num(minus_num):
    minus_num -= 1
    if minus_num < 0:
        minus_num = 1000000
        break

cnt = min(abs(plus_num - target_ch) + len(str(plus_num)), abs(minus_num - target_ch) + len(str(minus_num)))

if target_ch >= 100:
    cnt2 = target_ch - 100
else:
    cnt2 = 100 - target_ch

print(min(cnt, cnt2))