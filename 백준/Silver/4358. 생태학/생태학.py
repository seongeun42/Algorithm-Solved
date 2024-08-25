import sys
input = sys.stdin.readline

total = 0
tree = {}
while 1:
    name = input().rstrip()
    if name == "":
        break
    total += 1
    tree[name] = tree.get(name, 0) + 1
tree = sorted(list(tree.items()), key=lambda x: x[0])
for k, v in tree:
    print(f'{k} {(v / total * 100):.4f}')