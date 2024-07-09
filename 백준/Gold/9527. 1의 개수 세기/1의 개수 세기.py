def count(num, binary_one):
    cnt = 0
    bin_num = bin(num)[2:]
    for i in range(len(bin_num)):
        if bin_num[i] == '1':
            degree = len(bin_num) - i - 1
            cnt += binary_one[degree]
            num -= 2 ** degree
            cnt += num + 1
    return cnt

def solve():
    A, B = map(int, input().split())
    # 2^n - 1까지의 합
    binary_one = [0]
    leng = len(bin(B)[2:]) + 1
    for i in range(1, leng):
        binary_one.append(2 * binary_one[i - 1] + 2 ** (i - 1))
    print(count(B, binary_one) - count(A - 1, binary_one))

solve()