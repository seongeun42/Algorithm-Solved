def solve():
    N = int(input())
    size = [*map(int, input().split())]
    score = 0
    while len(size) > 1:
        size.sort()
        a, b = size.pop(), size.pop()
        score += a * b
        size.append(a + b)
    print(score)

solve()