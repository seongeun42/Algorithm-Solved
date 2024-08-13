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
            Set<Integer> b = new TreeSet<>();
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < an; i++) {
                a.add(Integer.parseInt(st.nextToken()));
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < bn; i++) {
                b.add(Integer.parseInt(st.nextToken()));
            }
            a.removeAll(b);
            System.out.println(a.size());
            for (int c : a)
                System.out.print(c + " ");
        }
}
