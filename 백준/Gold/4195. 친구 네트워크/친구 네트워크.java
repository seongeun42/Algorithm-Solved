import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int F = Integer.parseInt(br.readLine());
            Map<String, Integer> person = new HashMap<>();
            List<Integer> R = new ArrayList<>();
            List<Integer> cnt = new ArrayList<>();
            for (int i = 0; i < F; i++) {
                st = new StringTokenizer(br.readLine());
                String a = st.nextToken();
                String b = st.nextToken();
                boolean aExist = person.containsKey(a);
                boolean bExist = person.containsKey(b);
                if (!aExist && !bExist) {
                    person.put(a, person.size());
                    R.add(person.get(a));
                    person.put(b, person.size());
                    R.add(person.get(a));
                    cnt.add(2);
                    cnt.add(2);
                    sb.append(2).append("\n");
                } else if (!aExist) {
                    person.put(a, person.size());
                    int bRoot = findRoot(person.get(b), R);
                    R.add(bRoot);
                    cnt.set(bRoot, cnt.get(bRoot) + 1);
                    cnt.add(cnt.get(bRoot));
                    sb.append(cnt.get(bRoot)).append("\n");
                } else if (!bExist) {
                    person.put(b, person.size());
                    int aRoot = findRoot(person.get(a), R);
                    R.add(aRoot);
                    cnt.set(aRoot, cnt.get(aRoot) + 1);
                    cnt.add(cnt.get(aRoot));
                    sb.append(cnt.get(aRoot)).append("\n");
                } else {
                    int aRoot = findRoot(person.get(a), R);
                    int bRoot = findRoot(person.get(b), R);
                    int M = Math.max(aRoot, bRoot);
                    int m = Math.min(aRoot, bRoot);
                    if (aRoot != bRoot) {
                        cnt.set(m, cnt.get(m) + cnt.get(M));
                        R.set(M, m);
                    }
                    sb.append(cnt.get(m)).append("\n");
                }
            }
        }
        System.out.println(sb);
    }

    static int findRoot(int node, List<Integer> R) {
        if (R.get(node) != node)
            R.set(node, findRoot(R.get(node), R));
        return R.get(node);
    }

}