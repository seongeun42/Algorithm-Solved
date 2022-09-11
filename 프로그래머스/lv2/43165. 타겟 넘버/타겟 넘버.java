class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
    
    public int dfs(int[] numbers, int target, int hap, int dep) {
        if (dep == numbers.length)
            return hap == target ? 1 : 0;
        int cnt = 0;
        cnt += dfs(numbers, target, hap + numbers[dep], dep + 1);
        cnt += dfs(numbers, target, hap - numbers[dep], dep + 1);
        return cnt;
    }
}