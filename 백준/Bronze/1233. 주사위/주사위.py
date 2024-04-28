S1, S2, S3 = map(int, input().split())
hap = [0] * 81
ans = 0
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            v = i + j + k
            hap[v] += 1
            if hap[v] > hap[ans]:
                ans = v
            elif hap[v] == hap[ans] and v < ans:
                ans = v
print(ans)