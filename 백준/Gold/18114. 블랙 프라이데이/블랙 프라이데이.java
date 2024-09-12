import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int C = Integer.parseInt(st.nextToken());
    int[] w = new int[N];
    Set<Integer> weight = new HashSet<>();
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      w[i] = Integer.parseInt(st.nextToken());
      weight.add(w[i]);
      if (w[i] == C) {
        System.out.println(1);
        return;
      }
    }
    Arrays.sort(w);
    for (int i = 0; i < N; i++) {
      if (C - w[i] != w[i] && weight.contains(C - w[i])) {
        System.out.println(1);
        return;
      }
      for (int j = i + 1; j < N; j++) {
        Integer diff = C - w[i] - w[j];
        if (diff != w[i] && diff != w[j] && weight.contains(diff)) {
          System.out.println(1);
          return;
        }
      }
    }
    System.out.println(0);
  }

}