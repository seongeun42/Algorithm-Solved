import math
N = int(input())
S = input()
cnt = sum([1 for c in S if c != 'C'])
print(math.ceil((len(S) - cnt) / (cnt + 1)))