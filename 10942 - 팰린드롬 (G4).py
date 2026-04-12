import sys
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def check(i, j):
    if dp[i][j] < 0:
        if board[i] == board[j]:
            dp[i][j] = check(i+1, j-1)
        else:
            dp[i][j] = 0
    return dp[i][j]

n = int(input())
board = [0] + [int(i) for i in input().split()]

dp = [[-1]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i==j or i==j+1:
            dp[i][j]=1

q = int(input())
for _ in range(q):
    st, ed = map(int, input().split())
    print(check(st, ed))
    