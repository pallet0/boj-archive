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
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parent = [i for i in range(v+1)] # parent[n] = n이 속한 union의 대표값
size = [1 for i in range(v+1)] # size[n] = n이 속한 union의 크기
mst_weight = 0

def find(x):
    # x의 대표값은?
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    # x, y의 union을 합친다
    x = find(x)
    y = find(y)
    if size[x]>=size[y]: 
        parent[y] = x
        size[x] += size[y]
    else: 
        parent[x] = y
        size[y] += size[x]

v_cnt = 0
for weight, st, ed in sorted(edges):
    rs, re = find(st), find(ed)
    if rs != re:
        union(rs, re)
        mst_weight += weight
        v_cnt += 1
        if v_cnt == v - 1:
            break

print(mst_weight)
        