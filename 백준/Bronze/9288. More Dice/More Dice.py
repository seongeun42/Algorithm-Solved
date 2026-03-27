for t in range(int(input())):
    total = int(input())
    print(f"Case {t + 1}:")
    for i in range(1, 7):
        for j in range(i, 7):
            if i + j == total:
                print(f"({i},{j})")