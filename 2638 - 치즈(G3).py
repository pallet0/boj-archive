import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def check_empty(paper):
    for i in paper:
        for j in i:
            if j>0:
                return False
    return True

def flood(visited, paper, x, y):
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x+dx, y+dy

        if not (0<=nx<n and 0<=ny<m):
            continue
        if visited[nx][ny]:
            continue

        if paper[nx][ny] == 0:
            visited[nx][ny] = True
            flood(visited, paper, nx, ny)
        else:
            paper[nx][ny] += 1
            
    

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

turn = 0
while not check_empty(paper):
    visited = [[False]*m for _ in range(n)]

    flood(visited, paper, 0, 0)

    paper = [[0 if x>2 else min(x, 1) for x in row] for row in paper]
    turn += 1

print(turn)