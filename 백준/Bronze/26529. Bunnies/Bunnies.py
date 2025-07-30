t = int(input())
fi = [1, 1]
for i in range(2, 50):
    fi.append(fi[i - 2] + fi[i - 1])
for _ in range(t):
    n = int(input())
    print(fi[n])