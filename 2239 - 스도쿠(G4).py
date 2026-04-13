import sys
input = sys.stdin.readline

sdk = []
for _ in range(9):
    sdk.append(list(map(int, list(input().rstrip()))))

# 행 검사
def checkRow(i, num):
    for j in range(9):
        if sdk[i][j] == num:
            return False
    return True


# 열 검사
def checkCol(j, num):
    for i in range(9):
        if sdk[i][j] == num:
            return False
    return True

# 3x3칸 검사
def checkBox(i, j, num):
    x = (i//3)*3
    y = (j//3)*3
    for a in range(x, x+3):
        for b in range(y, y+3):
            if sdk[a][b] == num:
                return False
    return True

def check(i, j, num):
    return checkRow(i, num) and checkCol(j, num) and checkBox(i, j, num)

def put_valid(i, j):
    if j == 9:
        return put_valid(i+1, 0)
    elif i < 9:
        if sdk[i][j] == 0:
            for candidate in range(1, 10):
                if check(i, j, candidate):
                    sdk[i][j] = candidate
                    if put_valid(i, j+1):
                        return True
                    sdk[i][j] = 0
            return False
        else:
            return put_valid(i, j+1)
    else:
        return True

put_valid(0, 0)
for i in range(9):
    print(''.join(map(str, sdk[i])))