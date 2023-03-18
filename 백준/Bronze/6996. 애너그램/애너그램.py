n = int(input())
for _ in range(n):
    a, b = input().split()
    print(a, "&", b, "are ", end="")
    print("anagrams." if sorted(a) == sorted(b) else "NOT anagrams.")