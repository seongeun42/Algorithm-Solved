class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for (int i = 0; i < n; i++) {
            String line = Integer.toBinaryString(arr1[i] | arr2[i]);
            line = line.replace("0", " ");
            line = line.replace("1", "#");
            if (line.length() < n)
                line = " ".repeat(n - line.length()) + line;
            answer[i] = line;
        }
        
        return answer;
    }
}