import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = [[int(i) for i in input().split()] for _ in range(n)]

house = {}
cnt_h = 1
chicken = {}
cnt_c = 1


for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house[cnt_h] = (i, j)
            cnt_h += 1
        elif city[i][j] == 2:
            chicken[cnt_c] = (i, j)
            cnt_c += 1

chicken_dist = {}
for h in house:
    chicken_dist[h] = {}
    for c in chicken:
        chicken_dist[h][c] = abs(house[h][0] - chicken[c][0]) + abs(house[h][1] - chicken[c][1])
    chicken_dist[h] = sorted(chicken_dist[h].items(), key=lambda x: x[1])

best = float('inf')
for i in range(m, 0, -1):
    for closed in combinations(chicken.keys(), m):
        dists = []
        for h in house:
            for c, d in chicken_dist[h]:
                if c not in closed:
                    dists.append(d)
                    break
        if sum(dists) < best:
            best = sum(dists)

print(best)