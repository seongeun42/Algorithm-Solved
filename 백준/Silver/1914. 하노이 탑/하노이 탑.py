def hanoi(n, one, third) :
    if n == 1 :
        print(one, third)
        return
    hanoi(n - 1, one, 6 - one - third)
    print(one, third)
    hanoi(n - 1, 6 - one - third, third)

n = int(input())
print(2 ** n-1)
if n <= 20:
    hanoi(n, 1, 3)