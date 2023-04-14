from collections import deque

def diff(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    return cnt

def bfs(begin, target, words):
    q = deque([(begin, 0)])
    visit = [0] * len(words)
    while q:
        cw, dep = q.popleft()
        if diff(cw, target) == 1:
            return dep + 1
        for i in range(len(words)):
            if not visit[i] and diff(cw, words[i]) == 1:
                visit[i] = 1
                q.append((words[i], dep + 1))
    return 0

def dfs(word, target, words, visit, dep):
    if diff(word, target) == 1:
        return dep + 1
    ans = 0
    for i in range(len(words)):
        if not visit[i] and diff(word, words[i]) == 1:
            visit[i] = 1
            ans = dfs(words[i], target, words, visit, dep + 1)
    return ans
    
def solution(begin, target, words):
    if target not in words: return 0
    visit = [0] * len(words)
    return dfs(begin, target, words, visit, 0)
    # return bfs(begin, target, words)