import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        return bfs(numbers, target);
    }
    
    public int dfs(int[] numbers, int target, int hap, int dep) {
        if (dep == numbers.length)
            return hap == target ? 1 : 0;
        int cnt = 0;
        cnt += dfs(numbers, target, hap + numbers[dep], dep + 1);
        cnt += dfs(numbers, target, hap - numbers[dep], dep + 1);
        return cnt;
    }
    
    public int bfs(int[] numbers, int target) {
        Queue<Node> q = new LinkedList<>();
        int cnt = 0;
        q.offer(new Node(0, 0));
        while (!q.isEmpty()) {
            Node n = q.poll();
            if (n.i < numbers.length) {
                q.offer(new Node(n.i + 1, n.v + numbers[n.i]));
                q.offer(new Node(n.i + 1, n.v - numbers[n.i]));
            }
            else if (n.v == target)
                cnt++;
        }
        return cnt;
    }
    
    class Node {
        int i;
        int v;
        
        public Node(int i, int v) {
            this.i = i;
            this.v = v;
        }
    }
}

