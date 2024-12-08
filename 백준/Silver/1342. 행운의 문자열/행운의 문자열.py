def backtrack(dep, pre, alpa_cnt, max_len):
    global ans
    if dep == max_len:
        ans += 1
        return
    for c in alpa_cnt:
        if pre == c or alpa_cnt[c] == 0:
            continue
        alpa_cnt[c] -= 1
        backtrack(dep + 1, c, alpa_cnt, max_len)
        alpa_cnt[c] += 1

S = input()
alpa_cnt = {}
for c in S:
    alpa_cnt[c] = alpa_cnt.get(c, 0) + 1
ans = 0
backtrack(0, "", alpa_cnt, len(S))
print(ans)