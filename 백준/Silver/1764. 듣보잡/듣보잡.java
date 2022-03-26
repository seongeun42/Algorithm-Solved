import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashSet<String> noHear = new HashSet<String>();
        HashSet<String> noSee = new HashSet<String>();
        List<String> ans = new ArrayList<String>();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++)
            noHear.add(br.readLine());
        for (int j = 0; j < m; j++)
            noSee.add(br.readLine());

        noHear.retainAll(noSee);
        ans.addAll(noHear);
        Collections.sort(ans);

        System.out.println(ans.size());
        for (String v : ans)
            System.out.println(v);
    }
}