class Solution {
    public int solution(int[] array) {
        String s = "";
        for (int v : array) {
            s += Integer.toString(v);
        }
        return s.length() - s.replace("7", "").length();
    }
}