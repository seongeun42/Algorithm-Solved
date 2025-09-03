N, colors = int(input()), input()
b, r = 0, 0
if colors[0] == 'B':
    b += 1
else:
    r += 1
for i in range(1, N):
    if colors[i - 1] != colors[i]:
        if colors[i] == 'B':
            b += 1
        else:
            r += 1
print(1 + min(b, r))