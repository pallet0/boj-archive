import sys
input = sys.stdin.readline

sdk = [list(map(int, list(input().rstrip()))) for _ in range(9)]

rows = [0] * 9
cols = [0] * 9
boxes = [0] * 9
empties = []

for i in range(9):
    for j in range(9):
        v = sdk[i][j]
        if v == 0:
            empties.append((i, j))
        else:
            bit = 1 << v
            rows[i] |= bit
            cols[j] |= bit
            boxes[(i // 3) * 3 + j // 3] |= bit

def solve(k):
    if k == len(empties):
        return True
    i, j = empties[k]
    b = (i // 3) * 3 + j // 3
    used = rows[i] | cols[j] | boxes[b]
    for num in range(1, 10):
        bit = 1 << num
        if not (used & bit):
            sdk[i][j] = num
            rows[i] |= bit
            cols[j] |= bit
            boxes[b] |= bit
            if solve(k + 1):
                return True
            rows[i] ^= bit
            cols[j] ^= bit
            boxes[b] ^= bit
    sdk[i][j] = 0
    return False

solve(0)
sys.stdout.write('\n'.join(''.join(map(str, row)) for row in sdk) + '\n')
