#include <iostream>
using namespace std;
// [baekjoon] 10989번 - 수 정렬하기 3
// 2023.01.19


int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int n, tmp;
	cin >> n;

	int countArray[10001] = { 0 };

	for (int i = 0; i < n; i++) {
		cin >> tmp;
		countArray[tmp]++;
	}

	for (int i = 1; i < 10001; i++) {
		if (countArray[i] > 0) {
			for (int j = 0; j < countArray[i]; j++) {
				cout << i << "\n";
			}
		}
	}

	return 0;
}