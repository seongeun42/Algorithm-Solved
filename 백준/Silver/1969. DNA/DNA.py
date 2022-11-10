n, m = map(int, input().split())
dna = [input() for _ in range(n)]
s = ""
ans = 0
for i in range(m):
    acgt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n):
        acgt[dna[j][i]] += 1
    c, hap = 'A', 0
    for k, v in acgt.items():
        if v > hap:
            c, hap = k, v
    s += c
    ans += sum(acgt.values()) - hap
print(s, ans, sep='\n')