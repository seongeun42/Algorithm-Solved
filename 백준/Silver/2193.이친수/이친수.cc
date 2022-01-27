#include<iostream>
#include<vector>

using namespace std;

int main() {
	vector<long long> mem(91, 0);

	mem[1] = 1;
	mem[2] = 1;
	for (int i = 3; i < 91; i++) {
		mem[i] = mem[i - 1] + mem[i - 2];
	}
	int N;
	cin >> N;
	cout << mem[N];
}