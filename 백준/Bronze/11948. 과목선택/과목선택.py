science = sorted([int(input()) for _ in range(4)])
social = max(int(input()), int(input()))
print(sum(science[1:]) + social)