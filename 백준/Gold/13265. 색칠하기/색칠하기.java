import java.util.*;
import java.io.*;

public class Main {

  static ArrayList[] G;

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int T = Integer.parseInt(br.readLine());
    while (T-- > 0) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      G = new ArrayList[n + 1];
      for (int i = 0; i <= n; i++) {
        G[i] = new ArrayList<Integer>();
      }
      while (m-- > 0) {
        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        G[x].add(y);
        G[y].add(x);
      }
      int[] visited = new int[n + 1];
      String ans = "possible";
      for (int i = 1; i <= n; i++) {
        if (visited[i] == 0) {
          if (!bfs(i, visited)) {
            ans = "impossible";
            break;
          }
        }
      }
      sb.append(ans).append("\n");
    }
    System.out.println(sb);
  }

  static boolean bfs(int start, int[] visited) {
    Deque<Integer> q = new ArrayDeque<>();
    q.add(start);
    visited[start] = 1;
    while (!q.isEmpty()) {
      int cur = q.pollFirst();
      ArrayList<Integer> nextNodes = G[cur];
      for (Integer nxt : nextNodes) {
        if (visited[nxt] == 0) {
          visited[nxt] = -visited[cur];
          q.addLast(nxt);
        } else if (visited[nxt] == visited[cur]) {
          return false;
        }
      }
    }
    return true;
  }

}
