if __name__ == "__main__":
    while 1:
        a, b, c = sorted(map(int, input().split()))
        if a == b == c == 0:
            break
        if a + b <= c:
            print("Invalid")
        elif a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")