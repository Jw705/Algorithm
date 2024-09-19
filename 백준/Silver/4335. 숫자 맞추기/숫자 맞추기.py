import sys

input = sys.stdin.readline

is_stan_liar = False
high_arr = []
low_arr = []

while True:
    number = int(input())
    if number == 0:
        break

    oly_say = input().rstrip()
    if oly_say == "too high":
        high_arr.append(number)
    elif oly_say == "too low":
        low_arr.append(number)

    if oly_say == "right on":
        for num in low_arr:
            if num >= number:
                is_stan_liar = True
        for num in high_arr:
            if num <= number:
                is_stan_liar = True

        if is_stan_liar:
            print('Stan is dishonest')
        else:
            print('Stan may be honest')

        is_stan_liar = False
        high_arr = []
        low_arr = []