hurt = int(input())
max_cnt = int(input())
if hurt == 1:
    print(8 * max_cnt)
elif hurt == 2:
    print(4 * max_cnt + (3 if max_cnt % 2 else 1))
elif hurt == 3:
    print(4 * max_cnt + 2)
elif hurt == 4:
    print(4 * max_cnt + (1 if max_cnt % 2 else 3))
elif hurt == 5:
    print(8 * max_cnt + 4)