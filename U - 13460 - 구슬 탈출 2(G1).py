import sys
from collections import deque

n, m = map(int, input().split())
_ = input()
toy = [[c for c in input().rstrip()[1:-1]] for _ in range(n-2)]
_ = input()

pos = {'R': (0, 0), 'B': (0, 0), 'O': (0, 0)}

for i, r in enumerate(toy):
    for j, c in enumerate(r):
        if c == 'R':
            pos['R'] = (i, j)
            toy[i][j] = '.'
        elif c == 'B':
            pos['B'] = (i, j)
            toy[i][j] = '.'
        elif c == 'O':
            pos['O'] = (i, j)
            toy[i][j] = '.'

def bfs():
    q = deque([])