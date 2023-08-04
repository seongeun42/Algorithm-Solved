import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		int n = Integer.parseInt(br.readLine());
		int[] ds = new int[n];
		st = new StringTokenizer(br.readLine());
		int qcnt = 0;
		for (int i = 0; i < n; i++) {
			int qs = Integer.parseInt(st.nextToken());
			ds[i] = qs;
			if (qs == 0)
				qcnt++;
		}
		st = new StringTokenizer(br.readLine());
		int ccnt = Integer.parseInt(br.readLine());
		int[] q = new int[qcnt + ccnt];
		int qidx = ccnt;
		for (int i = 0; i < n; i++) {
			int v = Integer.parseInt(st.nextToken());
			if (ds[i] == 0)
				q[qidx++] = v;
		}
		st = new StringTokenizer(br.readLine());
		for (int i = ccnt - 1; i >= 0; i--) {
			q[i] = Integer.parseInt(st.nextToken());
		}
		for (int i = q.length - 1; i >= q.length - ccnt; i--) {
			sb.append(q[i]).append(" ");
		}
		System.out.println(sb);
	}
	
}