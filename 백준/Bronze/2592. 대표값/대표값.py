mb = {}
av = 0
for i in range(10):
    n = int(input())
    av += n
    if n in mb:
        mb[n] += 1
    else:
        mb[n] = 1
print(av // 10)
mb = sorted(mb.items(), key=lambda k: -k[1])
print(mb[0][0])