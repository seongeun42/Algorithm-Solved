t = int(input())
for _ in range(t):
    v, s = input().split()
    v = int(v)
    print(s[:v-1], s[v:], sep="")