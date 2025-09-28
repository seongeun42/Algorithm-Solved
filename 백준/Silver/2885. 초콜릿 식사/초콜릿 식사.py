K = int(input())
if K == 1:
    print(1, 0)
else:
    K = bin(K).replace("0b", '')
    if K.count('1') == 1:
        print(2 ** (len(K) - 1), 0)
    else:
        size = 2 ** len(K)
        cut = 0
        for i in range(len(K) - 1, -1 , -1):
            if K[i] == '1':
                cut = i + 1
                break
        print(size, cut)