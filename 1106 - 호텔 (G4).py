import sys
input = sys.stdin.readline

c, n = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(n)]

dp = [float('inf')] * (c+101) # dp[i] = 고객 i명을 얻는 데 필요한 최소 비용
dp[0] = 0

for cost, customer in cities:
    for w in range(customer, c+101):
        if dp[w-customer] + cost < dp[w]:
            dp[w] = dp[w-customer] + cost

print(min(dp[c:]))