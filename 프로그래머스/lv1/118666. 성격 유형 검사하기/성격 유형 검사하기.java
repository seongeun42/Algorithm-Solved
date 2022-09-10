import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int[] score = { 0, 3, 2, 1, 0, 1, 2, 3 };
        String type = "RTCFJMAN";
        Map<String, Integer> typeCnt = new HashMap<>();
        for (int i = 0; i < type.length(); i++)
            typeCnt.put(Character.toString(type.charAt(i)), 0);
        
        // 점수 구하기
        for (int i = 0; i < survey.length; i++) {
            String c = Character.toString(choices[i] < 4 ? survey[i].charAt(0) : survey[i].charAt(1));
            typeCnt.put(c, typeCnt.get(c) + score[choices[i]]);
        }
        
        // 유형 판별
        for (int i = 0; i < 8; i += 2) {
            String f = Character.toString(type.charAt(i));
            String s = Character.toString(type.charAt(i + 1));
            answer += typeCnt.get(f) >= typeCnt.get(s) ? f : s;
        }
        
        return answer;
    }
}