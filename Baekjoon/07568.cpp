#include <iostream>
#include <vector>
using namespace std;
// [baekjoon] 07568번 - 덩치
// 2023.01.31

int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	vector<int> v1;
	vector<int> v2;


	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		v1.push_back(x);
		v2.push_back(y);
	}

	for (int i = 0; i < n; i++) {
		int rank = 1;
		for (int j = 0; j < n; j++) {
			if (i != j && v1[i] < v1[j] && v2[i] < v2[j]) {
				rank++;
			}
		}
		cout << rank << " ";
	}

	return 0;
}

