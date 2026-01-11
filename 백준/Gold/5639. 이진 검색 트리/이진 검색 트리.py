import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

nodes = []
while 1:
    try:
        nodes.append(int(input()))
    except:
        break

def recursion(nodes):
    if len(nodes) == 0:
        return
    left, right = [], []
    root = nodes[0]
    for i in range(1, len(nodes)):
        if nodes[i] > root:
            left = nodes[1:i]
            right = nodes[i:]
            break
    else:
        left = nodes[1:]
    recursion(left)
    recursion(right)
    print(root)

recursion(nodes)