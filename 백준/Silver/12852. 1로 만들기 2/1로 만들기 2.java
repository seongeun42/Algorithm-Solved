import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int dpP[] = new int[n + 1];
        int dpC[] = new int[n + 1];

        for (int i = 2; i <= n; i++)
        {
            dpC[i] = dpC[i - 1] + 1;
            dpP[i] = i - 1;

            if (i % 3 == 0 && dpC[i] > dpC[i / 3])
            {
                dpC[i] = dpC[i / 3] + 1;
                dpP[i] = i / 3;
            }

            if (i % 2 == 0 && dpC[i] > dpC[i / 2])
            {
                dpC[i] = dpC[i / 2] + 1;
                dpP[i] = i / 2;
            }
        }

        System.out.println(dpC[n]);
        for (int i = n; i > 0; i = dpP[i])
            System.out.printf("%d ", i);
    }
}