y, m, d = map(int, input().split())
sy, sm, sd = map(int, input().split())
man = 0
if m < sm:
    man = sy - y
elif m == sm:
    man = sy - y if d <= sd else sy - y - 1
else:
    man = sy - y - 1
print(man)
print(sy - y + 1)
print(sy - y)