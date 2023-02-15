import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        my_string = my_string.toLowerCase();
        char[] chs = my_string.toCharArray();
        Arrays.sort(chs);
        return new String(chs);
    }
}