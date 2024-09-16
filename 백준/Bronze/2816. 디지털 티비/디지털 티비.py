import sys
input = sys.stdin.readline

n = int(input())
ch = [input().rstrip() for _ in range(n)]
kbs1 = ch.index("KBS1")
kbs2 = ch.index("KBS2")
if kbs1 == 0:
    print("1" * kbs2 + "4" * (kbs2 - 1))
elif kbs2 == 0:
    print("1" * kbs1 + "4" * kbs1)
elif kbs1 < kbs2:
    print("1" * kbs1 + "4" * kbs1, end="")
    print("1" * kbs2 + "4" * (kbs2 - 1))
else:
    print("1" * kbs2 + "4" * kbs2, end="")
    print("1" * kbs1 + "4" * kbs1, end="")