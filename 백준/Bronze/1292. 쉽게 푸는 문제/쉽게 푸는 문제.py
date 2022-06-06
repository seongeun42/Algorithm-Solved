A, B = map(int, input().split())
s = [0] + [i for i in range(46) for _ in range(i)]
print(sum(s[A:B + 1]))