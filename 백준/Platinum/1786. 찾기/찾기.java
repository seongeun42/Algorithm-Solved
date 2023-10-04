import java.io.*;
import java.util.*;

public class Main {
	
	static StringBuilder sb = new StringBuilder();
	static int ans = 0;
    
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String T = br.readLine();
		String P = br.readLine();
		kmp(T, P);
		System.out.println(ans);
		System.out.println(sb);
	}
	
	static void kmp(String str, String pattern) {
		int[] pi = makePi(pattern);
		int slen = str.length();
		int plen = pattern.length();
		int i = 0;
		for (int j = 0; j < slen; j++) {
			while (i > 0 && str.charAt(j) != pattern.charAt(i))
				i = pi[i - 1];
			
			if (str.charAt(j) == pattern.charAt(i)) {
				if (i == plen - 1) {
					sb.append(j - plen + 2).append(" ");
					ans++;
					i = pi[i];
				} else {
					i++;
				}
			}
		}
	}

	static int[] makePi(String pattern) {
		int len = pattern.length();
		int[] table = new int[len];
		int i = 0;
		for (int j = 1; j < len; j++) {
			while (i > 0 && pattern.charAt(j) != pattern.charAt(i))
				i = table[i - 1];
			 
			if (pattern.charAt(j) == pattern.charAt(i))
				table[j] = ++i;
		}
		return table;
	}
	
}