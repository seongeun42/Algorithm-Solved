def solution(stock_list):
    res = 0
    max_profit = stock_list[-1]
    stock_list = stock_list[::-1]

    for val in stock_list:
        if val > max_profit:
            max_profit = val
        else:
            res += max_profit - val

    return res

T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))
    print(solution(stock))