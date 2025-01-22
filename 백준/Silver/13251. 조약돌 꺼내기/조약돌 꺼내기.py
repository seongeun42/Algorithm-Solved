import math

M = int(input())
color = [*map(int, input().split())]
K = int(input())
total = sum(color)
prob = []
for c in color:
    prob.append(math.prod([c - i for i in range(K)]))
mo = math.prod([total - i for i in range(K)])
print(f"{sum(prob) / mo}")