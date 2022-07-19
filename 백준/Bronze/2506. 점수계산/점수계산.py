N = int(input())
s = [*map(int, input().split())]
total, plus = 0, 0
for v in s:
    if v == 1:
        plus += 1
        total += plus
    else:
        plus = 0
print(total)