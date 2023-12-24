#include <iostream>
using namespace std;
// [baekjoon] 10870번 - 피보나치 수 5
// 2023.01.26

int fibonacci(int n) {
	if (n <= 1) {
		return n;
	}
	else {
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
}

int main(void) {

	int n;
	cin >> n;

	cout << fibonacci(n);

	return 0;
}