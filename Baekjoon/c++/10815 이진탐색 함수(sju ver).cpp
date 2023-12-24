#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// [baekjoon] 10815번 - 숫자 카드
// 2023.01.31

void rFindElement(vector<int>& L, int k, int start, int end) {

	if (start > end) {		// base case
		cout << "0 ";
		return;				// k가 없는 경우
	}

	int mid = (start + end) / 2;

	if (L[mid] == k) {
		cout << "1 ";		// k를 찾은 경우
		return;
	}
	else if (L[mid] > k) {
		return rFindElement(L, k, start, mid - 1);
	}
	else {
		return rFindElement(L, k, mid + 1, end);
	}
}

void findElement(vector<int>& L, int k, int n) {
	return rFindElement(L, k, 0, n - 1);
}

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
		findElement(v1, tmp, n);
	}

	return 0;
}

