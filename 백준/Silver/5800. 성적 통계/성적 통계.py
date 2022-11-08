K = int(input())
for i in range(1, K + 1):
    c = [*map(int, input().split())]
    c = sorted(c[1:], reverse=True)
    gap = max([c[i - 1] - c[i] for i in range(1, len(c))])
    print("Class", i)
    print("Max ", c[0], ", Min ", c[-1], ", Largest gap ", gap, sep="")