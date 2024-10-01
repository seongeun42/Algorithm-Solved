import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        long queue1sum = 0;
        long queue2sum = 0;
        int total = queue1.length + queue2.length;
        
        for(int i = 0; i < queue1.length; i++) queue1sum += (long)queue1[i]; 
        for(int i = 0; i < queue2.length; i++) queue2sum += (long)queue2[i]; 
        
        if ((queue1sum + queue2sum) % 2 == 1)
            return -1;
        
        long dest = (queue1sum + queue2sum) / 2;
        int pointer1 = 0;
        int pointer2 = 0;
        boolean q1Switch = false;
        boolean q2Switch = false;
        int cnt = 0;
        while (queue1sum != queue2sum){
            if (cnt > 2 * total)
                return -1;
            if(queue1sum < queue2sum){
                if (!q2Switch) {
                    queue2sum -= (long)queue2[pointer2];
                    queue1sum += (long)queue2[pointer2++];
                } else {
                    queue2sum -= (long)queue1[pointer2];
                    queue1sum += (long)queue1[pointer2++];
                }
            }else {
                if (!q1Switch) {
                    queue1sum -= (long)queue1[pointer1];
                    queue2sum += (long)queue1[pointer1++];
                } else {
                    queue1sum -= (long)queue2[pointer1];
                    queue2sum += (long)queue2[pointer1++];
                }
            }
            cnt++;
            if(pointer2 == queue2.length) {
                pointer2 = 0;
                q2Switch = true;
            }
            if(pointer1 == queue1.length) {
                pointer1 = 0;
                q1Switch = true;
            }
        }
        return cnt;
    }
}