import sys

N = int(input())

input_list = []

for _ in range(N):
    input_list.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

sorted_list = sorted(input_list, key=lambda x: (x[1], x[0]))

end_time = 0
res = 0
for i in range(N):
    if end_time <= sorted_list[i][0]:
        res += 1
        end_time = sorted_list[i][1]

print(res)
"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""
