import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokedex_num = dict()
pokedex_name = dict()
for i in range(1, n + 1):
    pokemon_name = input().strip()
    pokedex_num[i] = pokemon_name
    pokedex_name[pokemon_name] = i

for _ in range(m):
    question = input().strip()
    if question in pokedex_name:
        print(pokedex_name[question])
    else:
        print(pokedex_num[int(question)])