import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

house = []
for _ in range(n):
    house.append([int(i) for i in input().split()])

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

pfier_up = next(i for i, row in enumerate(house) if row[0] == -1)
pfier_dn = pfier_up + 1

for _ in range(t):

    # 확산
    delta = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if house[y][x] > 0:
                div = house[y][x]//5
                for dx, dy in DIR:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<m and 0<=ny<n and house[ny][nx]>=0:
                        delta[ny][nx] += div
                        delta[y][x] -= div
    for y in range(n):
        for x in range(m):
            house[y][x] += delta[y][x]

    # 순환 - CCW
    house[pfier_up-1][0] = 0
    #   ↓
    for i in range(pfier_up-1, 0, -1):
        house[i][0] = house[i-1][0]
    #   ←
    for i in range(m-1):
        house[0][i] = house[0][i+1]
    #   ↑
    for i in range(pfier_up):
        house[i][m-1] = house[i+1][m-1]
    #   →
    for i in range(m-1, 1, -1):
        house[pfier_up][i] = house[pfier_up][i-1]
    house[pfier_up][1] = 0
    
    # 순환 - CW
    house[pfier_dn+1][0] = 0
    #   ↑
    for i in range(pfier_dn+1, n-1):
        house[i][0] = house[i+1][0]
    #   ←
    for i in range(m-1):
        house[n-1][i] = house[n-1][i+1]
    #   ↑
    for i in range(n-1, pfier_dn, -1):
        house[i][m-1] = house[i-1][m-1]
    #   →
    for i in range(m-1, 1, -1):
        house[pfier_dn][i] = house[pfier_dn][i-1]
    house[pfier_dn][1] = 0


dust = 0
for i in house:
    dust += sum(i)
print(dust+2)