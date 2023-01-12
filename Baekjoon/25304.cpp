#include <iostream>
using namespace std;
// [baekjoon] 25304번 - 영수증
// 2023.01.03

int main(void) {
	int x, n, a, b;
	int sum = 0;

	cin >> x >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		sum += a * b;
	}
	if (x == sum) {
		cout << "Yes";
	}
	else {
		cout << "No";
	}

	return 0;
}

/*
260000
4
20000 5
30000 2
10000 6
5000 8
*/