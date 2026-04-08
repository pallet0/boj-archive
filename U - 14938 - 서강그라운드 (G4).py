import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
item = [-1] + [int(i) for i in input().split()]

road = {}
for i in range(n):
    road[i+1] = []
for _ in range(m):
    u, v, w = input().split()
    road[u].append((v, w))
    road[v].append((u, w))
