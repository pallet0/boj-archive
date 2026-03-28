import sys
input = sys.stdin.readline

# 벨만포드: 정점 개수 V-1번 refresh 후 갱신되는 게 있다면 negative loop 존재

def solve():
    n, rd, wh = map(int, input().rstrip().split())
    graph = []

    # 길
    for _ in range(rd):
        u, v, w = map(int, input().rstrip().split())
        graph.append((u, v, w))
        graph.append((v, u, w))
    
    # 웜홀
    for _ in range(wh):
        u, v, w = map(int, input().rstrip().split())
        graph.append((u, v, -1*w))
    
    # 벨만포드
    for start in range(1, n+1):
        dist = [0]*(n+1)
        dist[start] = 0
        for _ in range(n):
            updated = False
            for u, v, w in graph:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u]+w
                    updated = True
            # early stop
            if not updated:
                return False

        # 음의 루프 체크
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                return True
    return False

tc = int(input())
for _ in range(tc):
    print("YES") if solve() else print("NO")