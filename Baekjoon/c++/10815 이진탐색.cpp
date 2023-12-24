#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// [baekjoon] 10815번 - 숫자 카드
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
		cout << binary_search(v1.begin(), v1.end(), tmp) << " ";
	}

	return 0;
}

