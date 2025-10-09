w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
av, am = divmod(p + t, w)
bv, bm = divmod(q + t, h)
x = w - am if av % 2 else am
y = h - bm if bv % 2 else bm
print(x, y)