T = int(input())
sub = [*map(int, input().split())]
if T < 5:
    sub += [0] * (5 - T)
total = 0
if sub[0] > sub[2]:
    total += (sub[0] - sub[2]) * 508
else:
    total += abs(sub[0] - sub[2]) * 108
if sub[1] > sub[3]:
    total += (sub[1] - sub[3]) * 212
else:
    total += abs(sub[1] - sub[3]) * 305
if sub[4] > 0:
    total += sub[4] * 707
print(total * 4763)