import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        ArrayList<Time> times = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            times.add(new Time(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        times.sort(Comparator.comparingInt((Time t) -> t.end).thenComparingInt((Time t) -> t.start));

        int ans = 0;
        int endTime = -1;
        for (int i = 0; i < n; i++) {
            if (endTime <= times.get(i).start) {
                ++ans;
                endTime = times.get(i).end;
            }
        }

        System.out.println(ans);
    }

    public static class Time {
        int start;
        int end;

        Time(int s, int e) {
            start = s;
            end = e;
        }

        public int compareTo(Time t) {
            return this.start - t.start;
        }
    }
}