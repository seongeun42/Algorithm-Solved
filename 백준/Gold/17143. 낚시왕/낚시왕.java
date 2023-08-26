import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = readInt(st), C = readInt(st), M = readInt(st);
        if (M == 0) {
            System.out.println(0);
            return;
        }

        int[] candi = new int[C];
        Arrays.fill(candi, R);
        Shark[][] sea = new Shark[R][C];
        Deque<Shark> sharks = new ArrayDeque<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = readInt(st) - 1, c = readInt(st) - 1;
            Shark shark = new Shark(r, c, readInt(st), readInt(st), readInt(st));
            sharks.add(shark);
            sea[r][c] = shark;
            if (candi[c] > r)
                candi[c] = r;
        }

        int cnt = -1;
        int ans = 0;
        while (++cnt < C) {
            if (candi[cnt] != R) {
                ans += sea[candi[cnt]][cnt].z;
                sea[candi[cnt]][cnt] = null;
            }
            Deque<Shark> list = new ArrayDeque<>();
            while (!sharks.isEmpty()) {
                Shark shark = sharks.poll();
                if (sea[shark.r][shark.c] == null)
                    continue;
                list.add(sea[shark.r][shark.c]);
                sea[shark.r][shark.c] = null;
            }
            int[] newCandi = new int[C];
            Arrays.fill(newCandi, R);
            while (!list.isEmpty()) {
                Shark shark = list.poll();
                shark.move(R, C);
                int r = shark.r, c = shark.c;
                if (newCandi[c] > r)
                    newCandi[c] = r;
                if (sea[r][c] == null || sea[r][c].z < shark.z)
                    sea[r][c] = shark;
                sharks.add(shark);
            }
            candi = newCandi;
        }
        System.out.println(ans);
    }

    static class Shark {
        int r, c, s, d, z;

        public Shark(int r, int c, int s, int d, int z) {
            this.r = r;
            this.c = c;
            this.s = s;
            this.d = d;
            this.z = z;
        }

        public void move(int R, int C) {
            int nr = r, nc = c, ns = s;
            switch (d) {
                case 1:
                    ns = s % ((R - 1) * 2);
                    nr = r - ns;
                    if (nr < 0) {
                        if (Math.abs(nr) >= R - 1) {
                            nr += 2 * (R - 1);
                        } else {
                            d = 2;
                            nr = Math.abs(nr);
                        }
                    }
                    r = nr;
                    return;
                case 2:
                    ns = s % ((R - 1) * 2);
                    nr = r + ns;
                    if (nr >= R) {
                        if (nr >= 2 * (R - 1)) {
                            nr -= 2 * (R - 1);
                        } else {
                            d = 1;
                            nr = 2 * (R - 1) - nr;
                        }
                    }
                    r = nr;
                    return;
                case 3:
                    ns = s % ((C - 1) * 2);
                    nc = c + ns;
                    if (nc >= C) {
                        if (nc >= 2 * (C - 1)) {
                            nc -= 2 * (C - 1);
                        } else {
                            d = 4;
                            nc = 2 * (C - 1) - nc;
                        }
                    }
                    c = nc;
                    return;
                case 4:
                    ns = s % ((C - 1) * 2);
                    nc = c - ns;
                    if (nc < 0) {
                        if (Math.abs(nc) >= C - 1) {
                            nc += 2 * (C - 1);
                        } else {
                            d = 3;
                            nc = Math.abs(nc);
                        }
                    }
                    c = nc;
                    return;
            }
        }
    }

    static int readInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

}