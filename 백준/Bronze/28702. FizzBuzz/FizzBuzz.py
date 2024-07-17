import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()
result_num = -1

if a.isdigit():
    result_num = int(a) + 3
elif b.isdigit():
    result_num = int(b) + 2
elif c.isdigit():
    result_num = int(c) + 1

if result_num % 3 == 0 and result_num % 5 == 0:
    print('FizzBuzz')
elif result_num % 3 == 0:
    print('Fizz')
elif result_num % 5 == 0:
    print('Buzz')
else:
    print(result_num)