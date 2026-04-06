import sys
input = sys.stdin.readline

n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int, input().split())))

# d[y][x][s] = (x, y) 좌표에서 s상태로 """시작되는""" 파이프가 0,0에서 올 수 있는 경우의 수 
d = [[{0: 0, 1: 0, 2: 0} for _ in range(n)] for _ in range(n)]

d[0][1][0] = 1

for _ in range(n):
    for y in range(n):
        for x in range(1, n):
            if x<n-1 and not house[y][x+1]: # 오른쪽이 빔
                d[y][x+1][0] = d[y][x][0] + d[y][x][2]
            if y<n-1 and not house[y+1][x]: # 아래가 빔
                d[y+1][x][1] = d[y][x][1] + d[y][x][2]
            if x<n-1 and y<n-1 and not 1 in [house[y+1][x], house[y][x+1], house[y+1][x+1]]: # 다 빔
                d[y+1][x+1][2] = d[y][x][0] + d[y][x][1] + d[y][x][2]

print(sum(d[n-1][n-1].values()))