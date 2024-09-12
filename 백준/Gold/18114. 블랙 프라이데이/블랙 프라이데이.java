import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int C = Integer.parseInt(st.nextToken());
    int[] w = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      w[i] = Integer.parseInt(st.nextToken());
      if (w[i] == C) {
        System.out.println(1);
        return;
      }
    }
    Arrays.sort(w);
    int l = 0, r = N - 1;
    while (l < r) {
      if (w[l] + w[r] == C) {
        System.out.println(1);
        return;
      } else if (w[l] + w[r] > C) {
        r--;
      } else {
        int diff = C - w[l] - w[r];
        if (diff != w[l] && diff != w[r] && binarySearch(l, r, diff, w)) {
          System.out.println(1);
          return;
        }
        l++;
      }
    }
    System.out.println(0);
  }

  static boolean binarySearch(int s, int e, int diff, int[] weight) {
    while (s <= e) {
      int mid = (s + e) / 2;
      if (weight[mid] == diff)
        return true;
      if (weight[mid] < diff) {
        s = mid + 1;
      } else {
        e = mid - 1;
      }
    }
    return false;
  }

}