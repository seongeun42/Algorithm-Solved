import java.io.*;
import java.util.*;

public class Main {
	
	static List<Blank> blanks = new ArrayList<>();
	static Set<Integer>[] square = new HashSet[9];
	static Set<Integer>[] row = new HashSet[9];
	static Set<Integer>[] col = new HashSet[9];
	static int[][] sudoqu = new int[9][9];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 9; i++) {
			square[i] = new HashSet<>();			
			row[i] = new HashSet<>();
			col[i] = new HashSet<>();
		}
		for (int i = 0; i < 9; i++) {
			String l = br.readLine();
			for (int j = 0; j < 9; j++) {
				int c = l.charAt(j) - '0';
				sudoqu[i][j] = c;
				if (c == 0) {
					blanks.add(new Blank(i, j));
				} else {
					row[i].add(c);
					col[j].add(c);
					square[(i / 3) * 3 + j / 3].add(c);
				}
			}
		}
		backtrack(0);
	}
	
	static boolean backtrack(int cnt) {
		if (cnt == blanks.size()) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					System.out.print(sudoqu[i][j]);
				}
				System.out.println();
			}
			return true;
		}
		
		Blank blank = blanks.get(cnt);
		int r = blank.r, c = blank.c;
		int sIdx = (r / 3) * 3 + (c / 3);
		for (int i = 1; i <= 9; i++) {
			if (row[r].contains(i) || col[c].contains(i) || square[sIdx].contains(i))
				continue;
			row[r].add(i);
			col[c].add(i);
			square[sIdx].add(i);
			sudoqu[r][c] = i;
			if (backtrack(cnt + 1))
				return true;
			sudoqu[r][c] = 0;
			square[sIdx].remove(i);
			col[c].remove(i);
			row[r].remove(i);
		}
		return false;
	}
	
	static class Blank {
		int r, c;
		
		Blank(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

}