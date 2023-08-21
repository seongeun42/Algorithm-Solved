import java.io.*;
import java.util.*;

public class Main {

	// R과 C, 도면 정보
	static int R, C;
	static char[][] map;

	// 상하좌우 방향 벡터
	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws Exception {
		// 입력 받기 위한 객체
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		// R과 C 입력받기
		st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		// 도면 정보 입력받기
		int mx = 0, my = 0; // 집 위치
		int zx = 0, zy = 0; // 유치원 위치
		map = new char[R][C];
		for (int i = 0; i < R; i++) {
			String line = br.readLine();
			for (int j = 0; j < C; j++) {
				map[i][j] = line.charAt(j);
				// 현 위치가 집이라면 좌표 저장
				if (line.charAt(j) == 'M') {
					mx = j;
					my = i;
				}
				// 현 위치가 유치원이라면 좌표 저장
				if (line.charAt(j) == 'Z') {
					zx = j;
					zy = i;
				}
			}
		}

		// M -> Z or Z -> M으로 이동하는 과정 중 나오는 빈칸 찾기
		int[] yx = search(mx, my);

		// 빈칸 사방에 있는 블록
		char[] block = new char[4];
		for (int i = 0; i < 4; i++) {
			int y = yx[0] + dy[i], x = yx[1] + dx[i];
			// 범위 내이고, 빈칸이 아니고 블록이라면 추가
			if (0 <= y && y < R && 0 <= x && x < C) {
				if (map[y][x] != '.' && map[y][x] != 'M' && map[y][x] != 'Z') {
					block[i] = map[y][x];
				} else {
					block[i] = ' ';
				}
			}
		}

		// 빈칸에 들어갈 블록 찾기
		boolean[] exist = existCheck(block);
		char ans = ' ';
		if (exist[0] & exist[1] & exist[2] & exist[3]) // 블록이 사방에 있으면 +
			ans = '+';
		else if (exist[0] & exist[1] & !exist[2] & !exist[3]) // 상하만 있으면 |
			ans = '|';
		else if (!exist[0] & !exist[1] & exist[2] & exist[3]) // 좌우만 있으면 -
			ans = '-';
		else if (!exist[0] & exist[1] & !exist[2] & exist[3]) // 하우만 있으면 1
			ans = '1';
		else if (exist[0] & !exist[1] & !exist[2] & exist[3]) // 상우만 있으면 2
			ans = '2';
		else if (exist[0] & !exist[1] & exist[2] & !exist[3]) // 상좌만 있으면 3
			ans = '3';
		else if (!exist[0] & exist[1] & exist[2] & !exist[3]) // 하좌만 있으면 4
			ans = '4';

		System.out.printf("%d %d %s", yx[0] + 1, yx[1] + 1, ans);
	}

	// 블록을 따라 이동할 함수
	static int[] search(int mx, int my) {
		// M 기준 시작 방향 찾기
		int d = -1;
		for (int i = 0; i < 4; i++) {
			int y = my + dy[i], x = mx + dx[i];
			// 범위 내이고, 블록이라면 그쪽으로 방향 정하기
			if (0 <= y && y < R && 0 <= x && x < C && map[y][x] != '.' && map[y][x] != 'Z') {
				d = i;
				break;
			}
		}
		// 다음 위치 값 저장할 변수
		int ny = my, nx = mx;
		// 블록을 따라 이동하며 빈칸을 만나면 해당 빈칸 위치 반환
		while (map[ny][nx] != '.') {
			ny += dy[d];
			nx += dx[d];
			if (0 <= ny && ny < R && 0 <= nx && nx < C) {
				// 빈칸이면 반환
				if (map[ny][nx] == '.')
					return new int[] { ny, nx };
				// 빈칸 아니면 방향 전환
				d = turn(d, map[ny][nx]);
			}
		}
		return null;
	}
	
	// 빈칸 블록 찾기
	static boolean[] existCheck(char[] b) {
		boolean[] chk = new boolean[4];
		if (b[0] == '|' || b[0] == '1' || b[0] == '+' || b[0] == '4')
			chk[0] = true;
		if (b[1] == '|' || b[1] == '2' || b[1] == '+' || b[1] == '3')
			chk[1] = true;
		if (b[2] == '-' || b[2] == '1' || b[2] == '+' || b[2] == '2')
			chk[2] = true;
		if (b[3] == '-' || b[3] == '3' || b[3] == '+' || b[3] == '4')
			chk[3] = true;
		return chk;
	}

	// 이동 방향 바꿀 함수
	static int turn(int d, char c) {
		switch (c) {
		case '1':
			// 기존 방향이 상이면 우, 좌면 하
			d = d == 0 ? 3 : 1;
			break;
		case '2':
			// 기존 방향이 하면 우, 좌면 상
			d = d == 1 ? 3 : 0;
			break;
		case '3':
			// 기존 방향이 하면 좌, 우면 상
			d = d == 1 ? 2 : 0;
			break;
		case '4':
			// 기존 방향이 상이면 왼, 우면 하
			d = d == 0 ? 2 : 1;
			break;
		}
		return d;
	}
	
}