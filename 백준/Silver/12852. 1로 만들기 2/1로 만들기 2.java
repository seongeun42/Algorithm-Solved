import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String dpP[] = new String[n + 1];
        int dpC[] = new int[n + 1];
        dpC[1] = 0;
        dpP[1] = "1";

        for (int i = 2; i <= n; i++)
        {
            dpC[i] = dpC[i - 1] + 1;
            dpP[i] = String.valueOf(i) + " " + dpP[i - 1];

            if (i % 3 == 0 && dpC[i] > dpC[i / 3])
            {
                dpC[i] = dpC[i / 3] + 1;
                dpP[i] = String.valueOf(i) + " " + dpP[i / 3];
            }

            if (i % 2 == 0 && dpC[i] > dpC[i / 2])
            {
                dpC[i] = dpC[i / 2] + 1;
                dpP[i] = String.valueOf(i) + " " + dpP[i / 2];
            }
        }

        System.out.println(dpC[n]);
        System.out.println(dpP[n]);
    }
}