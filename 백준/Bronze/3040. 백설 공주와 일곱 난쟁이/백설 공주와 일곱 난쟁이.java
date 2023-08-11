import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] nums = new int[9];
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            nums[i] = Integer.parseInt(br.readLine());
            sum += nums[i];
        }

        for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (sum - nums[i] - nums[j] == 100) {
                    for (int k = 0; k < 9; k++) {
                        if (k != i && k != j) {
                            sb.append(nums[k]).append("\n");
                        }
                    }
                    System.out.println(sb);
                    return;
                }
            }
        }
    }
}