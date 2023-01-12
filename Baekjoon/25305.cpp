#include <iostream>
#include <algorithm>
using namespace std;
// [baekjoon] 25305번 - 커트라인
// 2023.01.04

int main() {
	int arr[1001] = { 0 };
	int n, k, x;

	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n, greater<int>());

	cout << arr[k - 1] << "\n";

	return 0;
}