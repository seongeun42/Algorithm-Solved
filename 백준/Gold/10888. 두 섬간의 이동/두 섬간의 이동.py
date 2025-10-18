import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    connected = 0
    bridge_cnt = 0
    R = [-1] * (N + 1)
    bridge = [0, 0, 1]
    for i in range(2, N + 1):
        bridge.append(bridge[i] + i * (i + 1) // 2)
    for _ in range(N - 1):
        i = int(input())
        ir = find_root(i, R)
        jr = find_root(i + 1, R)
        if ir != jr:
            ir_cnt, jr_cnt = -R[ir], -R[jr]
            connected += ir_cnt * jr_cnt
            bridge_cnt += bridge[ir_cnt + jr_cnt] - bridge[ir_cnt] - bridge[jr_cnt]
            R[min(ir, jr)] += R[max(ir, jr)]
            R[max(ir, jr)] = min(ir, jr)
        print(connected, bridge_cnt)

solve()