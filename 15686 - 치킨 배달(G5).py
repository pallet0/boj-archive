import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = [[int(i) for i in input().split()] for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

best = 1e9
for combination in combinations(chicken, m):
    chicken_dist = 0
    for h in house:
        d = 1000
        for x, y in combination:
            d = min(d, abs(h[0] - x) + abs(h[1] - y))
        chicken_dist += d
    best = min(best, chicken_dist)

print(best)