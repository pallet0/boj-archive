import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, r, q = map(int, input().split())
rel = {i: [] for i in range(n+1)}

# 트리?
for _ in range(n-1):
    u, v = map(int, input().split())
    rel[u].append(v)
    rel[v].append(u)

# 진짜 트리
tree = {i: [] for i in range(n+1)}
def thisisatree(rel, node, parent):
    global tree
    for child in rel[node]:
        if child != parent:
            tree[node].append(child)
            thisisatree(rel, child, node)

thisisatree(rel, r, 0)

# DP: 한 트리의 노드 수는 (자기자신) + Σ(각 자손을 루트로 하는 서브트리의 노드 수)
dp = [0] * (n+1) # dp[n] = n을 루트로 하는 서브트리의 노드 수
def count(tree, root):
    global dp
    if not dp[root]:
        dp[root] = 1
        cnt = 0
        for child in tree[root]:
            cnt += count(tree, child)
        dp[root] += cnt
    
    return dp[root]

# 쿼리
for _ in range(q):
    query = int(input())
    print(count(tree, query))