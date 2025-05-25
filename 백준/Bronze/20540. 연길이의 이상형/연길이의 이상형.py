mbti = {'E': 'I', 'I': 'E', 'S': 'N', 'N': 'S', 'T': 'F', 'F': 'T', 'P': 'J', 'J': 'P'}
yg = input()
ans = ""
for c in yg:
    ans += mbti[c]
print(ans)