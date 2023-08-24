import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int typeCnt = Integer.parseInt(st.nextToken());
		int eatCnt = Integer.parseInt(st.nextToken());
		int coupon = Integer.parseInt(st.nextToken());
		int[] sushi = new int[N];
		for (int i = 0; i < N; i++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}

		int[] exist = new int[typeCnt + 1];
		exist[coupon]++;
		int eat = 1;

		for (int i = 0; i < eatCnt; i++) {
			if (exist[sushi[i]] == 0)
				eat++;
			exist[sushi[i]]++;
		}

		int s = 0, e = 0;
		int ans = eat;

		while (s < N) {
			exist[sushi[s]]--;
			if (exist[sushi[s++]] == 0)
				eat--;
			e = (s + eatCnt - 1) % N;
			exist[sushi[e]]++;
			if (exist[sushi[e]] == 1)
				eat++;
			if (ans < eat)
				ans = eat;
		}

		System.out.println(ans);
	}

}