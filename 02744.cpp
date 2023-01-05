#include <iostream>
#include <string>
using namespace std;
// [baekjoon] 2744번 - 대소문자 바꾸기
// 2023.01.04

int main() {
	string str;
	cin >> str;
	for (int i = 0; i < str.size(); i++) {
		if ('a' <= str[i] && str[i] <= 'z') {
			str[i] -= 32;
		}
		else {
			str[i] += 32;
		}
		cout << str[i];
	}
	return 0;
}