import sys
input = sys.stdin.readline

isbn = list(input().rstrip())

m = int(isbn.pop(-1))

s = 0
for i in range(12):
    if isbn[i] == '*':
        continue

    if i%2:
        s += int(isbn[i])*3
    else:
        s += int(isbn[i])

xm = (10 - (s%10) - m)%10
if not isbn.index('*')%2:
    print(xm)
else:
    print((xm*7)%10)