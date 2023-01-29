class Solution {
    public String[] solution(String my_str, int n) {
        int len = my_str.length();
        int cnt = len % n != 0 ? len / n + 1 : len / n;
        String[] answer = new String[cnt];
        for (int i = 0; i < len; i += n) {
            if (i + n < len)
                answer[i / n] = my_str.substring(i, i + n);
            else
                answer[i / n] = my_str.substring(i, len);
        }
        return answer;
    }
}