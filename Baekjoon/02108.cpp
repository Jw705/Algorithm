#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
// [baekjoon] 2108번 - 통계학
// 2023.01.22

int arr[800001] = { -5000 };

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int n;
	cin >> n;

	int sum = 0;

	int cntNumArr[8001] = { 0 };
	int maxCntNum = 0;			// (가장 작은) 최빈값
	int maxCntNum2nd = -1;		// 최빈값 중 두 번째로 작은 값

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		sum = sum + arr[i];
		cntNumArr[arr[i] + 4000]++;
	}

	// 최빈값 구하기
	for (int i = 1; i < 8001; i++) {
		if (cntNumArr[i] > cntNumArr[maxCntNum]) {
			maxCntNum = i;
			maxCntNum2nd = -1;
		}
		else if (cntNumArr[i] == cntNumArr[maxCntNum] && maxCntNum2nd == -1) {
			maxCntNum2nd = i;
		}
	}
	
	sort(arr, arr + n);

	cout << (int)round(double(sum) / n) << "\n";	// 산술평균
	cout << arr[n / 2] << "\n";						// 중앙값
	if (maxCntNum2nd == -1) {						// 최빈값
		cout << maxCntNum - 4000 << "\n";
	}
	else {
		cout << maxCntNum2nd - 4000 << "\n";
	}
	cout << arr[n - 1] - arr[0] << "\n";			// 범위


	return 0;
}