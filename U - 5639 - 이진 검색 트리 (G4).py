import sys

fw = []

for line in sys.stdin:
    tmp = line.strip()
    if not tmp:
        break
    fw.append(int(tmp))

fw.append(None)
fw.append(None)
fw.append(None)

idx = 0

def shuffle():
    global idx
    # 전위: 루트, 왼쪽, 오른쪽
    # 후위: 왼쪽, 오른쪽, 루트
    buffer = [fw[idx], fw[idx+1], fw[idx+2]]

    # 정상적인 트리는 buffer[1] < buffer[0] < buffer[2]
    # Case 1: buffer[1] > buffer[0] - buffer[1]이 새로운 오른쪽 트리, 왼쪽노드 없음
    if buffer[1] and buffer[1] > buffer[0]:
        idx+=1
        return shuffle() + [buffer[0]]
    
    # Case 2: buffer[0] > buffer[2] - buffer[1]이 새로운 왼쪽 트리
    if buffer[2] and buffer[0] > buffer[2]:
        idx+=1
        return shuffle() + shuffle() + [buffer[0]]
    
    # Case 3: buffer[1] < buffer[0] < buffer[2]를 만족하나, list가 다 안 끝남 -> 오른쪽 트리
    if fw[idx+3]:
        idx+=2
        return [buffer[1]] + shuffle() + [buffer[0]]
    
    # Case 4: 끝이다!
    return [buffer[1], buffer[2], buffer[0]]


bw = shuffle()
print(bw)