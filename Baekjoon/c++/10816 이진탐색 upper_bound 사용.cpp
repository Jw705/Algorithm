#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// [baekjoon] 10816번 - 숫자 카드 2
// 2023.01.31


int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	vector<int> v1;
	int n, m, tmp;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> tmp;
		v1.push_back(tmp);
	}

	sort(v1.begin(), v1.end());

	cin >> m;

	for (int i = 0; i < m; i++) {
		cin >> tmp;

		int upper = upper_bound(v1.begin(), v1.end(), tmp) - v1.begin();
		int lower = lower_bound(v1.begin(), v1.end(), tmp) - v1.begin();

		cout << upper - lower << " ";
	}

	return 0;
}

