#include <iostream>
using namespace std;
// [baekjoon] 2566번 - 최댓값
// 2023.01.04

int main() {
	int arr[10][10] = { 0 };
	int maxi = 0;
	int maxj = 0;

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> arr[i][j];
			if (arr[i][j] > arr[maxi][maxj]) {
				maxi = i;
				maxj = j;
			}
		}
	}
	cout << arr[maxi][maxj] << "\n" << maxi + 1 << " " << maxj + 1;


	return 0;
}