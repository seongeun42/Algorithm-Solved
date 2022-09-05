import java.util.*;

class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int right[] = {3, 2};
        int left[] = {3, 0};
        int coordi[][] = { {3, 1},
                          {0, 0}, {0, 1}, {0, 2},
                          {1, 0}, {1, 1}, {1, 2},
                          {2, 0}, {2, 1}, {2, 2} };
        
        for (int i : numbers) {
            if (i == 1 || i == 4 || i == 7) {
                answer += "L";
                left = coordi[i];
            }
            else if (i == 3 || i == 6 || i == 9) {
                answer += "R";
                right = coordi[i];
            }
            else {
                int l = Math.abs(coordi[i][0] - left[0]) + Math.abs(coordi[i][1] - left[1]);
                int r = Math.abs(coordi[i][0] - right[0]) + Math.abs(coordi[i][1] - right[1]);
                
                if (l == r) {
                    answer += hand.equals("left") ? "L" : "R";
                    if (hand.equals("left")) left = coordi[i];
                    else right = coordi[i];
                }
                else {
                    answer += l < r ? "L" : "R";
                    if (l < r) left = coordi[i];
                    else right = coordi[i];
                }
            }
        }
        
        return answer;
    }
}