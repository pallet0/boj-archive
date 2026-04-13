import sys
input = sys.stdin.readline

# 역추적?

fst = input().rstrip()
snd = input().rstrip()

if not fst or not snd:
    print(0)
    sys.exit(0)

# dp[i][j]: fst[:i+1]와 snd[:j+1]의 LCS 길이
dp = [[0]*(len(snd)+1) for _ in range(len(fst)+1)]

# 우리가 아는 lcs
for i in range(len(fst)):
    for j in range(len(snd)):
        if fst[i]==snd[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

cnt = dp[-1][-1]
print(cnt)

# 역추적
lcs = []
i, j = len(fst), len(snd)
while cnt > 0:
    while dp[i][j] == dp[i-1][j]:
        i-=1
    while dp[i][j] == dp[i][j-1]:
        j-=1
    lcs.append(fst[i-1])
    i, j = i-1, j-1
    cnt -= 1
print(''.join(reversed(lcs)))