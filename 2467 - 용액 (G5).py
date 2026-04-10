import sys
input = sys.stdin.readline

def bin_search(arr, target):
    # target 그 자체보다, target에 가장 가까운 값을 찾는다
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        elif arr[mid] > target:
            hi = mid - 1
        else:
            yield arr[mid]
            return
    if lo < len(arr): yield arr[lo] 
    if hi >= 0: yield arr[hi]

n = int(input())
sol = list(map(int, input().split()))
res = [2e9, 0, 0]

# 모든 sol의 값 i에 대해 -i와 가장 가까운 값을 찾고 더하여 기록한다

for solution in sol:
    ans = [2e9, 0, 0]
    for candidate in bin_search(sol, -solution):
        tmp = abs(solution + candidate)
        if candidate != solution and tmp < ans[0]:
            ans = [tmp, solution, candidate]
    res = min(res, ans, key=lambda x: x[0])

print(*sorted(res[1:]))