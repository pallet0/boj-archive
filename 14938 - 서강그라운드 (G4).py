import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [-1] + [int(i) for i in input().split()]

road = {}
for i in range(n):
    road[i+1] = []

for _ in range(r):
    u, v, w = map(int, input().split())
    road[u].append((v, w))
    road[v].append((u, w))

def dijk(graph, st):
    dist = [float('inf')] * (n+1)
    q = [(0, st)]

    dist[st] = 0

    while q:
        d, node = heappop(q)
        if dist[node] < d:
            continue
        
        for neighbor, weight in graph[node]:
            tmp = d + weight
            if dist[neighbor] > tmp:
                dist[neighbor] = tmp
                heappush(q, (tmp, neighbor))
    return dist

ccitem = [0] * (n+1) # ccitem: 노드 n에서 내렸을 때 모을 수 있는 아이템
for i in range(1, n+1):
    ccitem[i] = sum(item[j] if 0 < k <= m else 0 for j, k in enumerate(dijk(road, i))) + item[i]

print(max(ccitem))