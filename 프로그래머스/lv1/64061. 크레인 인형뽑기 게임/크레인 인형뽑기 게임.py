def solution(board, moves):
    answer = 0
    b = []
    
    for c in moves:
        for r in range(len(board)):
            if board[r][c - 1] != 0:
                pick = board[r][c - 1]
                board[r][c - 1] = 0
                if b and b[-1] == pick:
                    b.pop()
                    answer += 2
                else:
                    b.append(pick)
                break
        
    return answer