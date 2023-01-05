#include <iostream>
#include <algorithm>
using namespace std;
// [baekjoon] 2587번 - 대표값2
// 2023.01.04

int main() {
	int arr[101] = { 0 };
	int sum = 0;

	for (int i = 0; i < 5; i++) {
		cin >> arr[i];
		sum += arr[i];
	}
	sort(arr, arr + 5);

	cout << sum / 5 << "\n" << arr[2] << "\n";
	
	return 0;
}