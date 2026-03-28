import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

# g = {v: [(u, w), ...]}

def dijk(s, g, n):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    heap = [(0, s)] 

    while heap:
        d, ptr = heappop(heap)
        if d > dist[ptr]:
            continue
        for nextnode, weight in g[ptr]:
            new_dist = dist[ptr] + weight
            if new_dist < dist[nextnode]:
                dist[nextnode] = new_dist
                heappush(heap, (new_dist, nextnode))

    return dist

n, e = map(int, input().split())
g = {}
for i in range(1, n+1):
    g[i] = []

for _ in range(e):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))

p1, p2 = map(int, input().split()) 
from_1 = dijk(1, g, n)
from_p1 = dijk(p1, g, n)
from_p2 = dijk(p2, g, n)

sp1 = from_1[p1]
sp2 = from_1[p2]
p1p2 = from_p1[p2]
p2e = from_p2[n]
p1e = from_p1[n]

if float('inf') in [sp1, sp2, p1p2, p2e, p1e]:
    print(-1)
else:
    print(min(sp1 + p1p2 + p2e, sp2 + p1p2 + p1e))

# s(1) -> p1 -> p2 -> n
# s(1) -> p2 -> p1 -> n