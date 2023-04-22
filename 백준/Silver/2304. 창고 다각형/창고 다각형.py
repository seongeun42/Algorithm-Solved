import sys
input = sys.stdin.readline

n = int(input())
lh = sorted([[*map(int, input().split())] for _ in range(n)])[::-1]
ml, mh = max(lh, key=lambda x: x[1])
midx = lh.index([ml, mh])
llh, rlh = lh[:midx + 1][::-1], lh[midx:]
area = mh
cl, ch = llh.pop()
while llh:
    nl, nh = llh.pop()
    if ch < nh:
        area += abs(nl - cl) * ch
        cl, ch = nl, nh
    elif len(llh) == 0:
        area += abs(nl - cl) * ch
cl, ch = rlh.pop()
while rlh:
    nl, nh = rlh.pop()
    if ch < nh:
        area += abs(nl - cl) * ch
        cl, ch = nl, nh
    elif len(rlh) == 0:
        area += abs(nl - cl) * ch
print(area)