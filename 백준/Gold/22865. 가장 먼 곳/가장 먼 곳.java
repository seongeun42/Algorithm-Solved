import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N + 1];
        Arrays.fill(arr, Integer.MAX_VALUE);
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0])
                    return Integer.compare(o1[1], o2[1]);
                return Integer.compare(o1[0], o2[0]);
            }
        });
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 3; i++) {
            int l = Integer.parseInt(st.nextToken());
            int[] live = { 0, l };
            pq.offer(live);
            arr[l] = 0;
        }

        int M = Integer.parseInt(br.readLine());
        List<List<int[]>> G = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            G.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int D = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());
            G.get(D).add(new int[]{L, E});
            G.get(E).add(new int[]{L, D});
        }
        
        while (!pq.isEmpty()) {
            int[] cwn = pq.poll();
            if (arr[cwn[1]] < cwn[0])
                continue;
            for (int[] nwn : G.get(cwn[1])) {
                if (nwn[0] + cwn[0] < arr[nwn[1]]) {
                    arr[nwn[1]] = nwn[0] + cwn[0];
                    pq.offer(new int[]{ nwn[0] + cwn[0], nwn[1] });
                }
            }
        }

        int maxV = 0, ans = 0;
        for (int i = 1; i <= N; i++) {
            if (maxV < arr[i]) {
                maxV = arr[i];
                ans = i;
            }
        }
        System.out.println(ans);
    }

}