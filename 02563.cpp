#include <iostream>
using namespace std;
// [baekjoon] 2563번 - 색종이
// 2023.01.04

int main() {
	int arr[101][101] = { 0 };
	int n, a, b;
	int area = 0;

	cin >> n;
	for (int k = 0; k < n; k++) {
		cin >> a >> b;

		for (int i = a; i < a + 10; i++) {
			for (int j = b; j < b + 10; j++) {
				if (arr[i][j] == 0) {
					arr[i][j] = 1;
					area++;
				}
			}
		}

	}

	cout << area;
	
	return 0;
}