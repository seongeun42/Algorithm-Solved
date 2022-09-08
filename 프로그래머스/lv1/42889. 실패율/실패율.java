import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] notClear = new int[N + 2];
        double[][] failRates = new double[N][2];
        
        // 스테이지 별 도전자 수 구하기
        for (int i = 0; i < stages.length; i++)
            ++notClear[stages[i]];
        
        // 스테이지 실패율 구하기
        int people = notClear[N + 1]; // 도달자 수
        for (int i = N; i > 0; i--) {
            people += notClear[i];
            failRates[i - 1][0] = i;
            failRates[i - 1][1] = people != 0 ? (double) notClear[i] / people : 0;
        }
        
        // 정렬
        Arrays.sort(failRates, (f1, f2) -> Double.compare(-f1[1], -f2[1]));
        
        // 스테이지 넘버만 뽑기
        for (int i = 0; i < N; i++)
            answer[i] = (int) failRates[i][0];
        
        return answer;
    }
}