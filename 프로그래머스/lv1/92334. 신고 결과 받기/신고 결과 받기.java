import java.util.HashSet;
import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        // id의 인덱스 만들기
        HashMap<String, Integer> index = new HashMap<>();
        for (int i = 0; i < id_list.length; i++)
            index.put(id_list[i], i);
        
        // id 별 신고자 목록 구하기
        HashMap<Integer, HashSet<String>> user = new HashMap<>();
        for (String r : report) {
            String[] rs = r.split(" ");
            HashSet<String> reporters = user.getOrDefault(index.get(rs[1]), new HashSet<String>());
            reporters.add(rs[0]);
            user.put(index.get(rs[1]), reporters);
        }
        
        // 신고 메일 개수 세기
        for (Integer i : user.keySet()) {
            HashSet<String> reporters = user.get(i);
            if (reporters.size() >= k) {
                for (String id : reporters)
                    answer[index.get(id)]++;
            }
        }
        
        return answer;
    }
}