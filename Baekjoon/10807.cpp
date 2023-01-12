#include <iostream>
using namespace std;
// [baekjoon] 10807번 - 개수 세기
// 2023.01.04

int main(void) {
	int n, v;
	int cnt = 0;
	int arr[101] = { 0 };

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	cin >> v;
	for (int i = 0; i < n; i++) {
		if (arr[i] == v) {
			cnt++;
		}
	}
	cout << cnt;

	return 0;
}