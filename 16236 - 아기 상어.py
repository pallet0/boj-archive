import sys
input = sys.stdin.readline

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n = int(input())
tank = [[int(i) for i in input().split()] for _ in range(n)]

# 가장 가깝고 criterion보다 작은 물고기를 찾음
def findclosest(cur_x, cur_y, tank, criterion):
    dist = 0
    found = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[cur_x][cur_y] = True
    res = []

    q = [(cur_x, cur_y)]
    while q and not found:
        dist += 1
        nq = []
        for x, y in q:
            for dx, dy in DIRS:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and tank[nx][ny]<=criterion:
                    visited[nx][ny] = True
                    if 0 < tank[nx][ny] < criterion:
                        found = True
                        res.append((nx, ny))
                    else:
                        nq.append((nx, ny))
        q = nq
    return dist, res

# 시작점 찾기
x, y = -1, -1
for i in range(n):
    for j in range(n):
        if tank[i][j] == 9:
            x, y = i, j
tank[x][y] = 0

until_grow = 2
fishsize = 2
time = 0
while True:
    dist, (nx, ny) = (res:=findclosest(x, y, tank, fishsize))[0], \
        min(res[1], default=(-1, -1))

    # 엄마~~~~~~~~
    if nx < 0:
        break

    time += dist
    x, y = nx, ny
    tank[x][y] = 0
    until_grow-=1
    if until_grow == 0:
        fishsize+=1
        until_grow = fishsize

print(time)