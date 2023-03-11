class Solution {
    public int solution(String my_string) {
        String[] epr = my_string.split(" ");
        int answer = Integer.parseInt(epr[0]);
        for (int i = 2; i < epr.length; i += 2) {
            int op = epr[i - 1].equals("+") ? 1 : -1;
            answer += op * Integer.parseInt(epr[i]);
        }
        return answer;
    }
}