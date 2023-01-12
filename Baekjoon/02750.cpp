#include <iostream>
#include <algorithm>
using namespace std;
// [baekjoon] 2750번 - 수 정렬하기
// 2023.01.04

int main() {
	int arr[1001] = { 0 };
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