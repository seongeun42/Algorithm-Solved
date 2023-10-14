import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		String[][] arr = new String[N][M];
		for (int i = 0; i < N; i++) {
			arr[i] = br.readLine().split(" ");
		}
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < R; i++) {
			int c = Integer.parseInt(st.nextToken());
			int n = arr.length;
			int m = arr[0].length;
			switch (c) {
			case 1:
				verti(arr, n, m); break;
			case 2:
				horiz(arr, n, m); break;
			case 3:
				arr = rot90(arr, n, m, true); break;
			case 4:
				arr = rot90(arr, n, m, false); break;
			case 5:
				arr = moveSection(arr, n, m, true); break;
			case 6:
				arr = moveSection(arr, n, m, false); break;
			}
		}
		
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				sb.append(arr[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
	
	static void verti(String[][] arr, int n, int m) {
		for (int i = 0; i < n / 2; i++) {
			String[] tmp = arr[i];
			arr[i] = arr[n - i - 1];
			arr[n - i - 1] = tmp;
		}
	}

	static void horiz(String[][] arr, int n, int m) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m / 2; j++) {
				String tmp = arr[i][j];
				arr[i][j] = arr[i][m - j - 1];
				arr[i][m - j - 1] = tmp;
			}
		}
	}
	
	static String[][] rot90(String[][] arr, int n, int m, boolean mode) {
		String[][] after = new String[m][n];
		if (mode) { // 오른쪽
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					after[j][n - i - 1] = arr[i][j];
				}
			}
		} else { // 왼쪽
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					after[m - j - 1][i] = arr[i][j];
				}
			}
		}
		return after;
	}
	
	static String[][] moveSection(String[][] arr, int n, int m, boolean mode) {
		String[][] after = new String[n][m];
		if (mode) { // 시계
			for (int i = 0; i < n / 2; i++) {
				for (int j = 0; j < m / 2; j++) {
					after[i][m / 2 + j] = arr[i][j];
					after[n / 2 + i][j] = arr[n / 2 + i][m / 2 + j];
					after[n / 2 + i][m / 2 + j] = arr[i][m / 2 + j];
					after[i][j] = arr[n / 2 + i][j];
				}
			}
		} else { // 반시계
			for (int i = 0; i < n / 2; i++) {
				for (int j = 0; j < m / 2; j++) {
					after[i][j] = arr[i][m / 2 + j];
					after[n / 2 + i][m / 2 + j] = arr[n / 2 + i][j];
					after[i][m / 2 + j] = arr[n / 2 + i][m / 2 + j];
					after[n / 2 + i][j] = arr[i][j];
				}
			}
		}
		return after;
	}
	
}
