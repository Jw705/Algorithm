import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = input().rstrip().split()
    if len(a) == len(b):
        a_cnt_dict = {}
        b_cnt_dict = {}
        for c in a:
            if c in a_cnt_dict:
                a_cnt_dict[c] += 1
            else:
                a_cnt_dict[c] = 1
        for c in b:
            if c in b_cnt_dict:
                b_cnt_dict[c] += 1
            else:
                b_cnt_dict[c] = 1
        if a_cnt_dict == b_cnt_dict:
            print(a, '&', b, 'are anagrams.')
        else:
            print(a, '&', b, 'are NOT anagrams.')
    else:
        print(a, '&', b, 'are NOT anagrams.')