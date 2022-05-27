#include <vector>
#include <queue>

using namespace std;

int visited[100][100];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int M, N;

void bfs(int r, int c, vector<vector<int>>& pic, int& cnt, int& size) {
    queue<pair<int, int>> q;
    q.push(make_pair(c, r));
    visited[r][c] = 1;
    int color = pic[r][c];
    int loca = 1;
    
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (!(nx < 0 || nx >= N || ny < 0 || ny >= M))
            {
                if (!visited[ny][nx] && pic[ny][nx] == color)
                {
                    visited[ny][nx] = 1;
                    q.push(make_pair(nx, ny));
                    loca++;
                }
            }
        }
    }
    
    if (size < loca)
        size = loca;
    cnt++;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    for (int i = 0; i < 100; i++)
        for (int j = 0; j < 100; j++)
            visited[i][j] = 0;
    M = m;
    N = n;
    
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (!visited[i][j] && picture[i][j] != 0)
                bfs(i, j, picture, number_of_area, max_size_of_one_area);
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}