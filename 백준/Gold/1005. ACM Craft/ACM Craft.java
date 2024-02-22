import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test_case = Integer.parseInt(br.readLine());
        long time[];
        ArrayList<Integer>[] list;
        long totalTime[];
        int inDegree[];
        for(int tc = 1;  tc <= test_case ; tc ++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            time = new long[N + 1];
            list = new ArrayList[N+1];
            totalTime= new long[N+1];
            inDegree = new int[N+1];
            for(int i = 1; i <= N ; i++) {
                list[i] = new ArrayList<>();
                time[i] = Long.parseLong(st.nextToken());
            }

            for(int i = 0; i < K; i ++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                list[a].add(b);
                inDegree[b]++;
            }
            
            int t = Integer.parseInt(br.readLine());
            Queue<Integer> queue =new LinkedList<>();
            for (int i = 1; i <= N; i++) {
                if (inDegree[i] == 0) {
                    queue.add(i);
                    totalTime[i] = time[i];
                }
            }
            while (!queue.isEmpty()){
                int curr = queue.poll();
                if (curr == t) break;
                for(int a : list[curr]){
                    inDegree[a]--;
                    if(inDegree[a] == 0) queue.add(a);
                    if(totalTime[a] == 0L || totalTime[curr] + time[a] > totalTime[a]) {
                        totalTime[a] = totalTime[curr] + time[a];
                    }
                }
            }
            System.out.println(totalTime[t] == 0 ? time[t] : totalTime[t]);
        }
    }
}