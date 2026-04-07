import sys
sys.setrecursionlimit(10000)


fw = []

for line in sys.stdin:
    tmp = line.strip()
    if not tmp:
        break
    fw.append(int(tmp))

def rearrange(fw):
    if len(fw) == 1:
        return fw
    
    root = fw[0]

    # 둘중 하나는 무조건 nonzero
    lo = 0
    hi = 0
    
    for i in range(1, len(fw)):
        if hi == 0 and fw[hi] < fw[i]:
            hi = i
        if lo == 0 and fw[lo] > fw[i]:
            lo = i

    # case 오른쪽만
    if lo == 0:
        return rearrange(fw[hi:]) + [root]
    
    # case 왼쪽만
    if hi == 0:
        return rearrange(fw[lo:]) + [root]
    
    return rearrange(fw[lo:hi]) + rearrange(fw[hi:]) + [root]

res = rearrange(fw)
for i in res:
    print(i)