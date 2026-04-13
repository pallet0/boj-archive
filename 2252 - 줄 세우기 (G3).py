import sys
from collections import deque
input = sys.stdin.readline

# Kahn's algorithm???

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indeg = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a가 b보다 먼저 온다
    indeg[b] += 1

q = deque(i for i in range(1, n+1) if indeg[i] == 0)
res = []

while q:
    node = q.popleft()
    res.append(node)
    for nxt in graph[node]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            q.append(nxt)

print(*res)