import java.util.*;

class Solution {
    public int solution(String dartResult) {
        dartResult = dartResult.replace("10", "a");
        int answer = 0, cnt = -1;
        int[] num = new int[3];
        HashMap<Character, Integer> score = new HashMap<>();
        score.put('T', 3);
        score.put('D', 2);
        score.put('S', 1);
        
        for (int i = 0; i < dartResult.length(); i++) {
            char c = dartResult.charAt(i);
            if (Character.isDigit(c) || c == 'a')
                num[++cnt] = c != 'a' ? c - '0' : 10;
            else if (c == '*') {
                if (cnt != 0)
                   num[cnt - 1] *= 2;
                num[cnt] *= 2;
            }
            else if (c == '#')
                num[cnt] *= -1;
            else
                num[cnt] = (int) Math.pow(num[cnt], score.get(c));
        }
        
        for (int v : num)
            answer += v;
        
        return answer;
    }
    
}