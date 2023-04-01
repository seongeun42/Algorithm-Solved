n = int(input())
scores = [[*map(int, input().split())] for _ in range(n)]
s1 = [0] * 101
s2 = [0] * 101
s3 = [0] * 101
ans = [0] * n
for i in range(n):
    n1, n2, n3 = scores[i]
    s1[n1] += 1
    s2[n2] += 1
    s3[n3] += 1
for i in range(n):
    n1, n2, n3 = scores[i]
    if s1[n1] == 1:
        ans[i] += n1
    if s2[n2] == 1:
        ans[i] += n2
    if s3[n3] == 1:
        ans[i] += n3
print(*ans, sep="\n")