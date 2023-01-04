#include <iostream>
using namespace std;
// [baekjoon] 15552번 - 빠른 A+B
// 2023.01.04

int main(void) {
	int a, b, t;

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> a >> b;
		cout << a + b << "\n";
	}

	return 0;
}