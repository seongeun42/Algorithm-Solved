import java.util.*;

class Solution {
    public String solution(String s) {
        char[] ch = s.toCharArray();
        Arrays.sort(ch);
        String answer = "";
        for (int i = 0; i < ch.length; i++) {
            if (i != ch.length - 1 && ch[i] == ch[i + 1]) {
                while (i != ch.length - 1 && ch[i] == ch[i + 1]) {
                    i += 1;
                }
            }
            else {
                answer += Character.toString(ch[i]);
            }
        }
        return answer;
    }
}