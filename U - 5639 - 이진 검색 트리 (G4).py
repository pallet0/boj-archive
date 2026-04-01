import sys

fw = []

for line in sys.stdin:
    tmp = line.strip()
    if not tmp:
        break
    fw.append(int(tmp))

