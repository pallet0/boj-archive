import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

house = []
for _ in range(n):
    house.append([int(i) for i in input().split()])

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(t):

    # 확산
    for y in range(n):
        for x in range(m):
            if house[y][x] > 0:
                for dx, dy in DIR:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=nx<n and house[]