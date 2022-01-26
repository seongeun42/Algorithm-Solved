#include<iostream>
using namespace std;

int n, num[12], oper[4], cnt = 0;
int mi = 1000000000, ma = -1000000000;

int calc(int a, int b, int oper) {
	if (oper == 0) {
		return a + b;
	}
	else if (oper == 1) {
		return a - b;
	}
	else if (oper == 2) {
		return a * b;
	}
	else {
		return a / b;
	}
}

void func(int c, int tmp) {
	if (c == n-1) {
		mi = min(mi, cnt);
		ma = max(ma, cnt);
		cnt = 0;
		return;
	}
	for (int i = 0; i < 4; i++) {
		if (!oper[i]) continue;
		oper[i]--;
		cnt = calc(tmp, num[c + 1], i);
		func(c + 1, cnt);
		cnt = tmp;
		oper[i]++;
	}
}

int main(void) {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num[i];
	}
	for (int i = 0; i < 4; i++) {
		cin >> oper[i];
	}
	func(0, num[0]);
	cout << ma << '\n' << mi;

	return 0;
}