import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

prf = [0]
buffer = 0
for i in arr:
    buffer += i
    prf.append(buffer)
del buffer

l, r = 0, 0

minlen = 1e5+1
while l < n:
    if r > n:
        break
    acc = prf[r] - prf[l] # l번째 element 하나
    while acc < s:
        r += 1
        if r > n:
            break
        acc = prf[r] - prf[l]
    else:
        minlen = min(minlen, r - l)
    l += 1

print(minlen if minlen < 1e5+1 else 0)