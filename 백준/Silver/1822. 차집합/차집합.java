import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());
            int an, bn;
            an = Integer.parseInt(st.nextToken());
            bn = Integer.parseInt(st.nextToken());
            Set<Integer> a = new TreeSet<>();
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < an; i++) {
                a.add(Integer.parseInt(st.nextToken()));
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < bn; i++) {
                a.remove(Integer.parseInt(st.nextToken()));
            }
            StringBuilder sb = new StringBuilder();
            sb.append(a.size()).append("\n");
            for (Integer v : a) {
                sb.append(v).append(" ");
            }
            System.out.println(sb);
        }
}
