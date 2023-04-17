print("Gnomes:")
for _ in range(int(input())):
    ns = [*map(int, input().split())]
    print("Ordered" if ns == sorted(ns) or ns == sorted(ns, reverse=True) else "Unordered")