import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    StringTokenizer st = new StringTokenizer(br.readLine());
    int D = Integer.parseInt(st.nextToken());
    long cnt = 1, total = 0, actualNum = 1;
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < D; i++) {
      int num = Integer.parseInt(st.nextToken());
      actualNum = (actualNum - 1) * (i + 1) % 1_000_000_007 + num;
      sb.append((total + actualNum) % 1_000_000_007).append("\n");
      cnt = cnt * (i + 1) % 1_000_000_007;
      total = (total + cnt) % 1_000_000_007;
    }
    System.out.println(sb);
  }

}