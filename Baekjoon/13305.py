N = int(input())

length = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
res = length[0] * price[0] # 첫 도시에서 최소한 주유해야 하는 요금

for i in range(1, N-1):
    if min_price > price[i]:
        min_price = price[i]
    res += min_price * length[i] # 지나온 도시 중 가장 저렴한 도시에서 주유

print(res)
