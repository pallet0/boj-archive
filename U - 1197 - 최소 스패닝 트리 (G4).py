import sys
input = sys.stdin.readline

# 크루스칼: Union - Find
# 0. 모든 정점은 전부 서로 다른 팀
# (loop start)
# 1. 노드 A, B를 잇는 간선을 읽음
# 2. 노드 A, B가 서로 다른 팀이라면 간선을 챙김
#    노드 A, B가 같은 팀이라면 cycle이 형성되므로 무시
# (loop end)

v, e = map(int, input().split())
edges = []

for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

parent = [i for i in range(v+1)] # parent[n] = n이 속한 union의 대표값
mst = {i: [] for i in range(v+1)} # 기록용 최소신장트리

def find(x):
    # x의 대표값은?
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x, y):
    # x, y의 union을 합친다
    x = find(x)
    y = find(y)
    parent[y] = x

for weight, st, ed in sorted(edges):
    if find(st) != find(ed):
        union(st, ed)
        mst[st].append((ed, weight))
        mst[ed].append((st, weight))

print(parent)
print(mst)