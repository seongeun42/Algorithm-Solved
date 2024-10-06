N = int(input())
S = input()
sg, cy, hj = 0, 0, 0
i = 0
while i < len(S):
    for c in "ABC":
        if i >= len(S):
            break
        if S[i] == c:
            sg += 1
        i += 1
i = 0
while i < len(S):
    for c in "BABC":
        if i >= len(S):
            break
        if S[i] == c:
            cy += 1
        i += 1
i = 0
while i < len(S):
    for c in "CCAABB":
        if i >= len(S):
            break
        if S[i] == c:
            hj += 1
        i += 1
max_v = max(sg, cy, hj)
print(max_v)
if sg == max_v:
    print("Adrian")
if cy == max_v:
    print("Bruno")
if hj == max_v:
    print("Goran")