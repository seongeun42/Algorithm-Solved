import sys

def magic(k, card):
    arr = []
    for i in range(1, k + 2):
        arr.extend(card[:len(card) - 2 ** (k - i + 1)][::-1])
        card = card[len(card) - 2 ** (k - i + 1):]
    arr.extend(card[::-1])
    return arr[::-1]

N = int(input())
after = [*map(int, input().split())]
card = [k for k in range(1, N + 1)]
for i in range(1, 10):
    if N < 2 ** i: break
    mres = magic(i, card)
    for j in range(1, 10):
        if N < 2 ** j: break
        if magic(j, mres) == after:
            print(i, j)
            sys.exit()