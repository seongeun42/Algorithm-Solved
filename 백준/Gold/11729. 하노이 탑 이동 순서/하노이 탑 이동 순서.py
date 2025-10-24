N = int(input())

def hanoi(cnt, cur, desc, rest):
    if cnt == 1:
        print(cur, desc)
        return
    hanoi(cnt - 1, cur, rest, desc)
    print(cur, desc)
    hanoi(cnt - 1, rest, desc, cur)

print(sum([2 ** i for i in range(N)]))
hanoi(N, 1, 3, 2)