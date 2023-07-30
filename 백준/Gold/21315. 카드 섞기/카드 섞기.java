import java.io.*;
import java.util.*;

public class Main {

    public static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        String after = br.readLine();
        int[] card = new int[N];
        for (int i = 1; i <= N; i++) {
            card[i - 1] = i;
        }

        for (int i = 1; i < 10; i++) {
            if (N < Math.pow(2, i)) {
                break;
            }
            String mres = magic(i, card);
            for (int j = 1; j < 10; j++) {
                if (N < Math.pow(2, j)) {
                    break;
                }
                if (after.equals(magic(j, convert(mres)))) {
                    System.out.println(i + " " + j);
                    return;
                }
            }
        }
    }

    public static String magic(int k, int[] card) {
        String res = "";
        for (int i = 1; i < k + 2; i++) {
            for (int j = card.length - (int) Math.pow(2, k - i + 1) - 1; j >= 0; j--) {
                if (res.length() == 0) {
                    res += card[j];
                } else {
                    res = card[j] + " " + res;
                }
            }
            int[] tmp = new int[(int) Math.pow(2, k - i + 1)];
            int idx = 0;
            for (int j = card.length - (int) Math.pow(2, k - i + 1); j < card.length; j++) {
                tmp[idx++] = card[j];
            }
            card = tmp;
        }
        return card[0] + " " + res;
    }

    public static int[] convert(String nums) {
        return Arrays.stream(nums.split(" ")).mapToInt(Integer::parseInt).toArray();
    }

}