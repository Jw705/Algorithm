#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
// [baekjoon] 10814번 - 나이순 정렬
// 2023.01.06

struct member {
	int age;
	string name;
};

bool compare(member a, member b) {
	return a.age < b.age;	// b의 길이가 더 길도록 정렬 (=길이가 짧은 것이 앞으로)
}

int main() {
	member peoples[100001];
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> peoples[i].age >> peoples[i].name;
	}

	stable_sort(peoples, peoples + n, compare);

	for (int i = 0; i < n; i++) {
		cout << peoples[i].age << " " << peoples[i].name << "\n";
	}


	return 0;
}