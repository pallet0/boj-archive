import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

def bin_search(arr, target):
    # target이 들어갈 자리를 찾는다
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        elif arr[mid] > target:
            hi = mid - 1
        else:
            return mid
    return lo

# 도우미 행렬. c[k]=s라면, s는 길이 k+1의 LIS의 마지막 원소 중 가장 작은 값
# c의 길이는 LIS의 길이와 같다
c = [a[0]]

# 기록 행렬. r[k]=s라면, a[k]는 c의 s번째 원소였다는 걸 기록함
# c에서 LIS를 복원하는데 사용
r = [1]

# c, r 구성
for i in a[1:]:
    if i > c[-1]:
        c.append(i)
        r.append(len(c))
    else:
        idx = bin_search(c, i)
        c[idx] = i
        r.append(idx + 1)

print(len(c))

# LIS 복원
lis = []
ptr = n - 1
to_find = len(c)
while ptr >= 0:
    if r[ptr] == to_find:
        lis.append(a[ptr])
        to_find -= 1
    ptr -= 1
print(*reversed(lis))