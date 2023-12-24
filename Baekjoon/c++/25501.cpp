#include <iostream>
#include <string>
using namespace std;
// [baekjoon] 25501번 - 재귀의 귀재
// 2023.01.26

int recursion(string *str, int l, int r, int *cnt) {
	*cnt = *cnt + 1;
	if (l >= r) return 1;
	else if ((*str)[l] != (*str)[r]) return 0;
	else return recursion(str, l + 1, r - 1, cnt);
}

int isPalindrome(string *str, int *cnt) {
	return recursion(str, 0, (*str).size() - 1, cnt);
}

int main(void) {

	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int n;
	string str;			// 빈 문자열 str1 생성
	cin >> n;

	for (int i = 0; i < n; i++) {
		int cnt = 0;
		cin >> str;
		int res = isPalindrome(&str, &cnt);
		cout << res << " " << cnt << "\n";
	}

	return 0;
}