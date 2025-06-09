M, N = map(int, input().split())
num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
arr = []
for i in range(M, N + 1):
    s = str(i)
    eng = []
    for c in s:
        eng.append(num[int(c)])
    arr.append((" ".join(eng), i))
arr.sort()
for i in range(len(arr)):
    print(arr[i][1], end=" ")
    if (i + 1) % 10 == 0:
        print()