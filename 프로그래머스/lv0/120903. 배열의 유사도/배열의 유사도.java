import java.util.*;

class Solution {
    public int solution(String[] s1, String[] s2) {
        List<String> ns = new ArrayList<>(Arrays.asList(s1));
        ns.retainAll(Arrays.asList(s2));
        return ns.size();
    }
}