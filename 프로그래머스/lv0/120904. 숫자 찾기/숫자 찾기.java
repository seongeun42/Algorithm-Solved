class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        for (int i = Integer.toString(num).length(); num > 0; i--) {
            if (num % 10 == k) {
                answer = i;
            }
            num /= 10;
        }
        return answer;
    }
}