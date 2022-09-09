import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int pick = 0;
        Stack<Integer> b = new Stack<>();
        
        for (int c : moves) {
            // 인형 나올 때까지
            for (int r = 0; r < board.length; r++) {
                if (board[r][c - 1] != 0) {
                    // 뽑기
                    pick = board[r][c - 1];
                    board[r][c - 1] = 0;
                    // 바구니 제일 위의 인형과 같으면 터트림
                    if (b.size() != 0 && b.peek().equals(pick)) {
                        answer += 2;
                        b.pop();
                    } else {
                        // 다르면 넣기
                        b.push(pick);
                    }
                    break;
                }
            }
        }       
        return answer;
    }
}