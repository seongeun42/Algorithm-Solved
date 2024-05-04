import sys
input = sys.stdin.readline

R, C, ZR, ZC = map(int, input().split())
ans = []
for _ in range(R):
    line = input().rstrip()
    new_line = []
    for c in line:
        new_line.append(c * ZC)
    for _ in range(ZR):
        ans.append(new_line)
for i in range(len(ans)):
    print("".join(ans[i]))