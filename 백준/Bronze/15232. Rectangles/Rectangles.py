r, c = int(input()), int(input())
print(*["*" * c for  _ in range(r)], sep="\n")