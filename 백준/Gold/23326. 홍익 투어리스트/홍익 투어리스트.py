import sys
input = sys.stdin.readline

# 1. 펜윅 트리 업데이트 (idx 위치에 val만큼 더하기)
def update(idx, val):
    idx += 1  # 펜윅 트리는 1-based index 사용
    while idx <= N:
        tree[idx] += val
        idx += (idx & -idx)

# 2. 펜윅 트리 쿼리 (0부터 idx까지의 합 구하기)
def query(idx):
    idx += 1
    s = 0
    while idx > 0:
        s += tree[idx]
        idx -= (idx & -idx)
    return s

# 3. 구간 합 구하기 (left ~ right 사이의 명소 개수)
def query_range(left, right):
    if left > right: return 0
    return query(right) - query(left - 1)

def solve():
    global N, tree
    N, Q = map(int, input().split())
    A = [*map(int, input().split())]
    
    # 펜윅 트리 초기화
    tree = [0] * (N + 1)
    
    # 초기 명소 등록
    for i in range(N):
        if A[i] == 1:
            update(i, 1)
            
    cur = 0
    
    for _ in range(Q):
        q = input().split()
        
        if len(q) == 1: # 가장 가까운 명소 찾기
            # 전체 명소 개수가 0이면 -1
            if query(N - 1) == 0:
                print(-1)
                continue
            
            found = False
            dist = float('inf')
            
            # 1. 현재 위치(cur) ~ 끝(N-1) 사이에 명소가 있는지 확인 (오른쪽 탐색)
            if query_range(cur, N - 1) > 0:
                # 이분 탐색으로 가장 가까운 위치 찾기
                lo, hi = cur, N - 1
                res = N - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if query_range(cur, mid) > 0: # cur ~ mid 사이에 명소가 있으면
                        res = mid
                        hi = mid - 1  # 더 가까운 곳을 찾아 범위를 좁힘
                    else:
                        lo = mid + 1
                dist = res - cur
                found = True
            
            if not found: # 오른쪽에 없으면 원형으로 돌아서 0 ~ cur-1 탐색
                if query_range(0, cur - 1) > 0:
                    lo, hi = 0, cur - 1
                    res = 0
                    while lo <= hi:
                        mid = (lo + hi) // 2
                        if query_range(0, mid) > 0: # 0 ~ mid 사이에 명소가 있으면
                            res = mid   # 가능한 앞쪽을 잡아야 함
                            hi = mid - 1
                        else:
                            lo = mid + 1
                    dist = (N - cur) + res
            
            print(dist)

        else:
            cmd, val = map(int, q)
            if cmd == 1: # 명소 ON/OFF
                idx = val - 1
                # 현재 상태를 확인 (구간합 이용: 해당 위치만 1인지 확인)
                is_on = query_range(idx, idx)
                
                if is_on: # 켜져 있으면 끈다 (-1)
                    update(idx, -1)
                else:     # 꺼져 있으면 켠다 (+1)
                    update(idx, 1)
            else: # 이동
                cur = (cur + val) % N

solve()