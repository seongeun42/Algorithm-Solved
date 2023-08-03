import java.io.*;
import java.util.*;

public class Main {

	static int[] acgt = new int[4], acgtCnt = new int[4];
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int sLen = Integer.parseInt(st.nextToken());
		int pLen = Integer.parseInt(st.nextToken());
		String s = br.readLine();
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 4; i++) {
			acgt[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < pLen; i++) {
			++acgtCnt[idx(s.charAt(i))];
		}
		int ans = check();
		for (int i = pLen; i < sLen; i++) {
			--acgtCnt[idx(s.charAt(i - pLen))];
			++acgtCnt[idx(s.charAt(i))];
			ans += check();
		}
		System.out.println(ans);
	}
	
	public static int check() {
		for (int i = 0; i < 4; i++) {
			if (acgt[i] > acgtCnt[i])
				return 0;
		}
		return 1;
	}
	
	public static int idx(char v) {
		switch (v) {
		case 'A':
			return 0;
		case 'C':
			return 1;
		case 'G':
			return 2;
		case 'T':
			return 3;
		}
		return 0;
	}
	
}