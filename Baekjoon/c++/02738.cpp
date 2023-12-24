#include <iostream>
using namespace std;
// [baekjoon] 2738번 - 행렬 덧셈
// 2023.01.04

int main() {
	int n, m;
	int a[101][101] = { 0 };
	int b[101][101] = { 0 };
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> b[i][j];
			b[i][j] += a[i][j];
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << b[i][j];
			if (j + 1 != m) {
				cout << " ";
			}
		}
		cout << "\n";
	}

	return 0;
}