import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long s = 1, e = (long) n * times[times.length - 1];
        
        while (s <= e) {
            long mid = (s + e) / 2;
            long cnt = 0;
            for (int t : times)
                cnt += mid / t;
            
            if (cnt >= n) {
                e = mid - 1;
                answer = mid;
            } else {
                s = mid + 1;
            }
        }
        
        return answer;
    }
}