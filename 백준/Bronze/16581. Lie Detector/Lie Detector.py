import sys
input = sys.stdin.readline

t = int(input())
test = [input().strip() for _ in range(t)][::-1]
flag = True if test[0] == "TRUTH" else False
for s in test[1:]:
    if flag:
        flag = True if s == "TRUTH" else False
    else:
        flag = False if s == "TRUTH" else True
print("TRUTH" if flag else "LIE")