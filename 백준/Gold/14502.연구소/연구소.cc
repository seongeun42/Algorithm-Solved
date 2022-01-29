#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int N, M;
int map[8][8];
int testmap[8][8];
vector<pair<int, int>> emptys;
vector<pair<int, int>> viruses;
int ans = -1;

void maketestmap() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			testmap[i][j] = map[i][j];
		}
	}
}

int calculatesize() {
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (testmap[i][j] == 0) cnt++;
		}
	}
	return cnt;
}

void bfs() {
	queue<pair<int, int>> q;
	for (int i = 0; i < viruses.size(); i++) {
		q.push(viruses[i]);
	}

	while (!q.empty()) {
		int ti = q.front().first;
		int tj = q.front().second;
		q.pop();

		//위쪽으로 갈 수 있고, 빈 공간 이라면
		if (ti - 1 >= 0 && testmap[ti - 1][tj] == 0) {
			testmap[ti - 1][tj] = 2;
			q.push({ ti - 1, tj });
		}
		//아래쪽으로 갈 수 있고, 빈 공간 이라면
		if (ti + 1 < N && testmap[ti + 1][tj] == 0) {
			testmap[ti + 1][tj] = 2;
			q.push({ ti + 1, tj });
		}
		//왼쪽으로 갈 수 있고, 빈 공간 이라면
		if (tj - 1>= 0 && testmap[ti][tj - 1] == 0) {
			testmap[ti][tj - 1] = 2;
			q.push({ ti, tj - 1});
		}
		//오른쪽으로 갈 수 있고, 빈 공간 이라면
		if (tj + 1 < M && testmap[ti][tj + 1] == 0) {
			testmap[ti][tj + 1] = 2;
			q.push({ ti, tj + 1 });
		}
	}
}

vector<pair<int, int>> nC3;
void comb(int start){
	if (nC3.size() == 3) {
		for (int i = 0; i < 3; i++) {
			int ni = nC3[i].first;
			int nj = nC3[i].second;
			testmap[ni][nj] = 1;
		}
		bfs();
		int tmpans = calculatesize();
		//printf("tmpans: %d\n", tmpans);
		if (tmpans > ans) ans = tmpans;
		//printf("ans: %d\n", ans);
		maketestmap();
		//return을 꼭! 넣어줘야 한다
		return;
	}

	for (int i = start; i < emptys.size(); i++) {
		nC3.push_back(emptys[i]);
		comb(i + 1);
		nC3.pop_back();
	}
}

int main() {
	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &map[i][j]);
			if (map[i][j] == 0) emptys.push_back({ i, j });
			if (map[i][j] == 2) viruses.push_back({ i, j });
		}
	}
	maketestmap();
	comb(0);
	printf("%d", ans);
}