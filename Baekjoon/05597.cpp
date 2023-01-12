#include <iostream>
using namespace std;
// [baekjoon] 5597번 - 과제 안 내신 분..?
// 2023.01.04

int main(void) {
	int tmp;
	int arr[31] = { 0 };

	for (int i = 0; i < 28; i++) {
		cin >> tmp;
		arr[tmp] = 1;
	}
	for (int i = 1; i < 31; i++) {
		if (arr[i] == 0) {
			cout << i << "\n";
		}
	}
	return 0;
}