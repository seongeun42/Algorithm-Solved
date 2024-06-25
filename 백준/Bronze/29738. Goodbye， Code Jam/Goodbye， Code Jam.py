T = int(input())
for i in range(T):
    N = int(input())
    ans = "Round 1"
    if N <= 25:
        ans = "World Finals"
    elif N <= 1000:
        ans = "Round 3"
    elif N <= 4500:
        ans = "Round 2"
    print(f"Case #{i + 1}: {ans}")