import sys
input = sys.stdin.readline

def find(k, words):
    for i in range(k):
        for j in range(k):
            if i == j: continue
            hap = words[i] + words[j]
            if hap == hap[::-1]:
                return hap
    return 0            

def solve():
    T = int(input())
    for _ in range(T):
        k = int(input())
        words = [input().strip() for _ in range(k)]
        print(find(k, words))

solve()