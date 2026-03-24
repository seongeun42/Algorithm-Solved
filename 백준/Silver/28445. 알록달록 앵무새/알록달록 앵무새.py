color = set(input().split())
color |= set(input().split())
color = sorted(list(color))
for c1 in color:
    for c2 in color:
        print(c1, c2)