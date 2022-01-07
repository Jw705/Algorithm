#include <iostream>
#include <algorithm>
using namespace std;
// [SWExpertAcademy] 2063. 중간값 찾기
// 2023.01.06

int main() {
	int arr[201] = { 0 };
	int n;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	sort(arr, arr + n);

	cout << arr[n / 2];

	return 0;
}