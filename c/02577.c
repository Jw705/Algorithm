#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 2577번 - 숫자의 개수

int main() {	

	int a, b, c;
	int num[10] = { 0 };

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	int abc = a * b * c;

	while (abc > 0) {
		int n = abc % 10;
		num[n]++;
		abc /= 10;
	}
	
	for (int i = 0; i < 10; i++) {
		printf("%d\n", num[i]);
	}
}