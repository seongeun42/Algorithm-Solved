N = int(input())
C = {'A': "000000", 'B': "001111", 'C': "010011", 'D': "011100",
     'E': "100110", 'F': "101001", 'G': "110101", 'H': "111010"}
S = input()
ans = ""
for i in range(0, len(S), 6):
    c = S[i:i+6]
    find = False
    for key, val in C.items():
        cnt = 0
        for j in range(6):
            if c[j] != val[j]:
                cnt += 1
                if cnt > 1:
                    break
        if cnt <= 1:
            ans += key
            find = True
            break
    if not find:
        ans = i // 6 + 1
        break
print(ans)