s = [*map(int, input().split())]
hap = sum(s[:4])
print(max(0, 4 * s[-1] - hap))