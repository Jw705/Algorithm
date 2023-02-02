#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
// [baekjoon] 14425번 - 문자열 집합
// 2023.02.01

int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	vector<string> v;
	int n, m;
	string tmp;
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> tmp;
		v.push_back(tmp);
	}

	sort(v.begin(), v.end());

	int cnt = 0;
	for (int i = 0; i < m; i++) {
		cin >> tmp;
		cnt += binary_search(v.begin(), v.end(), tmp);
	}

	cout << cnt;

	return 0;
}

