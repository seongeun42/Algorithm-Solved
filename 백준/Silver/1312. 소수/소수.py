A, B, N = map(int, input().split())
res = 0
for i in range(N) :
    A = (A % B) * 10
    res = A // B
print(res)