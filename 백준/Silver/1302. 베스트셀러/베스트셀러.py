from collections import defaultdict
n = int(input())
book = defaultdict(int)
for _ in range(n):
    book[input()] += 1
book = sorted(list(book.items()), key=lambda x: [-x[1], x[0]])
print(book[0][0])