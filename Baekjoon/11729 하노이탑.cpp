#include <iostream>
#include <string>
#include <cmath>
using namespace std;
// [baekjoon] 11729번 - 하노이 탑 이동 순서
// 2023.01.31

string str;

void hanoi(int n, char from, char aux, char to) {
	if (n == 1) {
		cout << from << " " << to << "\n";
		return;
	}
	hanoi(n - 1, from, to, aux);
	cout << from << " " << to << "\n";
	hanoi(n - 1, aux, from, to);
}

int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int n;
	cin >> n;
	cout << (int)pow(2, n) - 1 << '\n';

	hanoi(n, '1', '2', '3');

	return 0;
}

