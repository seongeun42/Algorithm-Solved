N = input()
left, right = map(int, N[:len(N) // 2]), map(int, N[len(N) // 2:])
print("LUCKY" if sum(left) == sum(right) else "READY")