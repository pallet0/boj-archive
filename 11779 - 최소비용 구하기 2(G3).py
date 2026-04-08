import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
m = int(input())

# map
d = {}

for i in range(1, n+1):
    d[i] = []

for _ in range(m):
    u, v, w = map(int, input().split())
    d[u].append((v, w))

#
def dijk(graph: dict, st: int):
    dist = [float('inf')] * (n+1)
    prev = [0] * (n+1) # prev[n] -> n의 최단경로상 직전 노드
    dist[st] = 0

    q = []
    heappush(q, (0, st))

    while q:
        ndist, node = heappop(q)
        if dist[node] < ndist:
            continue

        for neighbor, weight in graph[node]:
            distance = ndist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = node
                heappush(q, (distance, neighbor))

    return dist, prev


st, ed = map(int, input().split())

distmap, prev = dijk(d, st)

path = []
cur = ed
while cur != st:
    path.append(cur)
    cur = prev[cur]
path.append(st)
path.reverse()

print(distmap[ed])
print(len(path))
print(*path)