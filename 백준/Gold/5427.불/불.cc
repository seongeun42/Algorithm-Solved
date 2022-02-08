#include <cstdio>
#include <queue>
#include <memory.h>
using namespace std;

int T, W, H;
char arr[1001][1001];
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

struct QUE {
    int r, c, t, data;
};

int BFS(void)
{
    queue<QUE> q;
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (arr[i][j] == '@') {
                q.push({i, j, 0, '@'});
            }
        }
    }
    for (int i=0; i<H; i++) {
        for (int j=0; j<W; j++) {
            if (arr[i][j] == '*') {
                q.push({i, j, 0, '*'});
            }
        }
    }
    while(!q.empty()) {
        int row=q.front().r, col=q.front().c;
        int time=q.front().t; char cur=q.front().data;
        q.pop();
        if (arr[row][col] == '@' && (row == 0 || row == H-1 || col == 0 || col == W-1)) return time+1;
        for (int i=0; i<4; i++){
            int nr = row + dr[i], nc = col + dc[i];

            if (nr < 0 || nr >= H || nc < 0 || nc >= W) continue;

            if (cur == '@' && arr[nr][nc] == '.') {
                q.push({nr, nc, time+1, '@'});
                arr[nr][nc] = '@';
            }
            else if (cur == '*' && (arr[nr][nc] == '.' || arr[nr][nc] == '@')) {
                q.push({nr, nc, time+1, '*'});
                arr[nr][nc] = '*';
            }
        }
    }

    return -1;
}

int main(void)
{
    int ans = 0;
    scanf("%d", &T);
    for (int t=0; t<T; t++) {
        ans = 0;
        memset(arr, 0, sizeof(arr));
        scanf("%d %d", &W, &H);

        for (int i=0; i<H; i++) {
            scanf("%s", &arr[i]);
        }

        ans = BFS();
        if (ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}