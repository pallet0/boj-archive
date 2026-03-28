import sys
input = sys.stdin.readline

# 편의상 heap[0] = None

def is_min(i):
    return (i.bit_length() - 1) % 2 == 0

def push(heap: list, val):
    heap.append(val)
    idx = len(heap)-1

    if idx == 1: return
    parent = idx//2

    if is_min(idx):                    # Min Level
        if heap[idx] > heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            bubble_up_max(heap, parent)
        else:
            bubble_up_min(heap, idx)
    else:                                # Max Level
        if heap[idx] < heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            bubble_up_min(heap, parent)
        else:
            bubble_up_max(heap, idx)


def bubble_up_min(heap: list, idx):
    while True:
        grandparent = idx // 4
        if grandparent < 1 or heap[idx] >= heap[grandparent]:
            break
        heap[idx], heap[grandparent] = heap[grandparent], heap[idx]
        idx = grandparent

def bubble_up_max(heap: list, idx):
    while True:
        grandparent = idx // 4
        if grandparent < 1 or heap[idx] <= heap[grandparent]:
            break
        heap[idx], heap[grandparent] = heap[grandparent], heap[idx]
        idx = grandparent

def pop(heap: list, cmd):
    # cmd == -1 : 최소값 pop
    # cmd == 1  : 최대값 pop
    if len(heap) == 1:
        return

    if cmd == -1:
        heap[1] = heap[-1]
        heap.pop()
        if len(heap) > 1:
            trickle_down(heap, 1)
    else:
        if len(heap) == 2: # 원소 1개
            return heap.pop()
        toremove = 2 if len(heap) == 3 or heap[2]>heap[3] else 3
        heap[toremove] = heap[-1]
        heap.pop()
        if toremove < len(heap):
            trickle_down(heap, toremove)


def trickle_down(heap, idx):
    if is_min(idx):
        trickle_down_min(heap, idx)
    else:
        trickle_down_max(heap, idx)

def trickle_down_min(heap, idx):
    n = len(heap)
    children = []
    for c in [idx*2, 1+idx*2]:
        if c < n:
            children.append(c)
            for gc in [c*2, 1+c*2]:
                if gc < n:
                    children.append(gc)
    if not children: return # nowhere to trickle down

    m = min(children, key=lambda x: heap[x])

    # if gc:
    if m >= idx*4:
        if heap[m] < heap[idx]:
            heap[m], heap[idx] = heap[idx], heap[m]
            if heap[m] > heap[m//2]:
                heap[m], heap[m//2] = heap[m//2], heap[m]
            trickle_down_min(heap, m)
    else:
        if heap[m] < heap[idx]:
            heap[m], heap[idx] = heap[idx], heap[m]

def trickle_down_max(heap,idx):
    n = len(heap)
    children = []
    for c in [idx*2, 1+idx*2]:
        if c < n:
            children.append(c)
            for gc in [c*2, 1+c*2]:
                if gc < n:
                    children.append(gc)
    if not children: return # nowhere to trickle down

    m = max(children, key=lambda x: heap[x])

    # if gc:
    if m >= idx*4:
        if heap[m] > heap[idx]:
            heap[m], heap[idx] = heap[idx], heap[m]
            if heap[m] < heap[m//2]:
                heap[m], heap[m//2] = heap[m//2], heap[m]
            trickle_down_max(heap, m)
    else:
        if heap[m] > heap[idx]:
            heap[m], heap[idx] = heap[idx], heap[m]


testcase = int(input())
for _ in range(testcase):
    k = int(input())
    heap = [None]

    for _ in range(k):
        cmd, val = input().split()
        val = int(val)

        if cmd == "I":
            push(heap, val)
        elif cmd == "D":
            pop(heap, val)
        # print(f"CURRNET HEAP:\n\t{heap}")
    
    if len(heap) == 1:
        print("EMPTY")
    elif len(heap) == 2:
        print(heap[1], heap[1])
    elif len(heap) == 3:
        print(heap[2], heap[1])
    else:
        print(max(heap[2], heap[3]), heap[1])