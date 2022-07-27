#pragma warning(disable:4996)
#include <stdio.h>
// [baekjoon] 1929번 - 소수 구하기

int main() {

	int num[1000001] = { 1,1, 0 };

	int m, n;

	scanf("%d %d", &m, &n);
	

	for (int i = 2; i <= n; i++) {
		if (num[i] == 0) {
			for (int j = 2; i*j <= n; j++) {
				num[i*j] = 1;
			}
		}
	}

	for (int i = m; i <= n; i++) {
		if (num[i] == 0) printf("%d\n", i);
	}
}
