#include <iostream>
using namespace std;
// [baekjoon] 2525�� - ���� �ð�

int main(void) {
	int a, b, c;
	cin >> a >> b >> c;

	b += c;
	while (b >= 60) {
		a++;
		b -= 60;
	}
	if (a >= 24) {
		a -= 24;
	}

	cout << a << " " << b;
	return 0;
}

/*
14 30
20
*/