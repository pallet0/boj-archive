import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
    
n = int(input())
sol = list(map(int, input().split()))
sol.sort()

# 하나 고정, 투 포인터로 접근
# cur = sols[i]+sols[j]가 -control에 가장 가까워져야됨
# i+=1이면 cur 증가, j-=1이면 sol 감소는 자명
# i>=j가 될때까지 반복

ans = [3e9+1, 0, 0, 0]
for c in range(n):
    # print(f"{sol[c]} 통제중")
    control = sol[c]
    i, j = 0, n-1
    if c==0: i+=1
    if c==n-1: j-=1
    while 0<=i<j<n:

        tmp = abs(sol[i]+sol[j]+control)
        if ans[0] > tmp:
            # print(f"\t 갱신!")
            ans = [tmp, control, sol[i], sol[j]]

        # print(f"\t현재 {sol[i]}, {sol[j]} 확인 중")
        cur = sol[i] +sol[j] + control
        if cur<0:
            i+=1
            while i==c or i==j: i+=1
        elif cur>0:
            j-=1
            while j==c or j==i: j-=1
        
        if cur == 0 and i!=c and j!=c: 
            break
    # print(f"{control} 통제: 최적은 {ans[2]}, {ans[3]}")

print(*sorted(ans[1:]))