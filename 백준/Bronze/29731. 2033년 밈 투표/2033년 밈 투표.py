import sys
input = sys.stdin.readline

N = int(input())
Strs = [input().strip() for _ in range(N)]
li = {"Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you",
     "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you",
     "Never gonna stop"}
ans = "No"
for s in Strs:
    if s not in li:
        ans = "Yes"
        break
print(ans)