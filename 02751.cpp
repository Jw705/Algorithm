#include <iostream>
#include <algorithm>
using namespace std;
// [baekjoon] 2751번 - 수 정렬하기 2
// 2023.01.04

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int arr[1000001] = { 0 };
	int n;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);
	for (int i = 0; i < n; i++) {
		cout << arr[i] << "\n";
	}

	return 0;
}