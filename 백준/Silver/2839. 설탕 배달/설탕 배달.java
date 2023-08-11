import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        if (N % 5 != 0) {
            for (int i = N / 5; i >= 0; i--) {
                int temp = N - i * 5;
                if (temp % 3 == 0) {
                    System.out.println(temp / 3 + i);
                    return;
                } else if (i == 0) {
                    System.out.println(-1);
                    return;
                }
            }
        }
        System.out.println(N / 5);
    }

}