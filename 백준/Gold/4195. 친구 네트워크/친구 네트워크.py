import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find_root(R, n):
    if R[n] != n:
        R[n] = find_root(R, R[n])
    return R[n]

def solve():
    t = int(input())
    for _ in range(t):
        person = {}
        R = []
        cnt = []
        f = int(input())
        for _ in range(f):
            a, b = input().split()
            if a not in person and b not in person:
                person[a] = len(person)
                R.append(person[a])
                person[b] = len(person)
                R.append(person[a])
                cnt.append(2)
                cnt.append(2)
                print(2)
            elif a not in person:
                person[a] = len(person)
                br = find_root(R, person[b])
                R.append(br)
                cnt[br] += 1
                cnt.append(cnt[br])
                print(cnt[br])
            elif b not in person:
                person[b] = len(person)
                ar = find_root(R, person[a])
                R.append(ar)
                cnt[ar] += 1
                cnt.append(cnt[ar])
                print(cnt[ar])
            else:
                ar = find_root(R, person[a])
                br = find_root(R, person[b])
                M, m = max(ar, br), min(ar, br)
                if ar != br:
                    cnt[m] += cnt[M]
                    R[M] = m
                print(cnt[m])

solve()